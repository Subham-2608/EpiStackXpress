import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os

# ─────────────────────────────────────────────────────────────────────────────
# CRITICAL: define predict_expression BEFORE any pickle.load()
# ─────────────────────────────────────────────────────────────────────────────
def predict_expression(X_new, model):
    if isinstance(X_new, np.ndarray):
        X_new = pd.DataFrame(X_new, columns=model["feature_cols"])
    else:
        X_new = X_new[model["feature_cols"]]
    svm_p = model["svm_model"].predict(X_new)
    xgb_p = model["xgb_base"].predict(X_new)
    return model["meta"].predict(np.column_stack([svm_p, xgb_p]))

# Inject into __main__ so pickle can resolve it on load
import __main__
__main__.predict_expression = predict_expression

# ─────────────────────────────────────────────────────────────────────────────
# Model paths
# ─────────────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_REGISTRY = {
    "Control": os.path.join(BASE_DIR, "..", "static", "models", "stacking_ensemble_Mock.pkl"),
    "Treatment": os.path.join(BASE_DIR, "..", "static", "models", "stacking_ensemble_RB.pkl"),
}

# ─────────────────────────────────────────────────────────────────────────────
# Page config
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="EpiStackXpress: Epigenetic Stacking Ensemble for Gene eXpression",
    initial_sidebar_state="expanded",
    layout="wide",
)

# ─────────────────────────────────────────────────────────────────────────────
# Header
# ─────────────────────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns([1.5, 20, 2])
with col1:
    st.image("static/images/icarlogo.png", width=150)
with col2:
    st.markdown(
        "<h1 style='text-align:center;'>"
        "EpiStackXpress: Epigenetic Stacking Ensemble for Gene eXpression"
        "</h1>",
        unsafe_allow_html=True,
    )
with col3:
    st.image("static/images/iasri-logo.png", width=150)

st.markdown("---")

col_instr, col_img = st.columns([1, 1.5])
with col_instr:
    st.markdown("### Instructions for Users")
    st.markdown(
        """
        <p style='text-align: justify;'>
        <b>1. File Format:</b> Upload a CSV file generated using the recommended feature engineering workflow illustrated on the right. Each row should correspond to a single gene (or transcript), while each column should contain the engineered features required by the prediction model.
        <br><br>
        <b>2. Required Columns:</b> Ensure that the uploaded file contains all feature columns used during model training and that they appear in the exact same order as expected by the model.
        <br><br>
        <b>3. Choose Condition:</b> Select the appropriate experimental condition before prediction. Choose <i>Control</i> for untreated samples or <i>Treatment</i> for stress conditions (e.g., Rice Black-Streaked Dwarf Virus infection) to load the corresponding stacking ensemble model.
        <br><br>
        <b>4. Output:</b> The application predicts the <b>log₂(FPKM + 1)</b> expression value for each gene or transcript in the uploaded dataset using the selected stacking ensemble model.
        <br><br>
        <b>5. Supported Organisms:</b> The tool is primarily developed for <i>Oryza sativa</i> and may also be applicable to related plant species with compatible feature representations.
        </p>
        """,
        unsafe_allow_html=True
    )
with col_img:
    st.image("static/images/Instructions.png", use_container_width=True)

st.markdown("---")

# ─────────────────────────────────────────────────────────────────────────────
# Sidebar — condition selector
# ─────────────────────────────────────────────────────────────────────────────
col_sel1, col_sel2, col_sel3 = st.columns([1, 1, 1])
with col_sel1:
    selected_condition = st.selectbox(
        "⚙️ Select Experimental Condition",
        list(MODEL_REGISTRY.keys()),
    )

st.markdown("---")
    
# ─────────────────────────────────────────────────────────────────────────────
# Load model (cached so it loads only once per condition)
# ─────────────────────────────────────────────────────────────────────────────
@st.cache_resource
def load_model(condition):
    path = MODEL_REGISTRY[condition]
    if not os.path.exists(path):
        return None, f"Model file not found:\n`{path}`"
    try:
        with open(path, "rb") as f:
            model = pickle.load(f)
        return model, None
    except Exception as e:
        return None, str(e)

model, load_error = load_model(selected_condition)

# ─────────────────────────────────────────────────────────────────────────────
# Main layout
# ─────────────────────────────────────────────────────────────────────────────
col_upload, col_results = st.columns([1, 2])

with col_upload:
    st.subheader("📂 Upload Feature CSV")

    if load_error:
        st.error(f"**Model load failed:**\n\n{load_error}")
        st.stop()

    # Show model metadata
    with st.expander("ℹ️ Loaded Model Info"):
        meta_info = model["metadata"]
        st.write(f"**Condition** : {selected_condition}")
        st.write(f"**Organism** : {meta_info['organism']}")
        st.write(f"**Number of features** : {meta_info['n_features']}")

    uploaded_csv = st.file_uploader(
        "Upload gene feature CSV",
        type=["csv"],
        help="Must contain all model feature columns.",
    )

    if uploaded_csv is not None:
        try:
            input_df = pd.read_csv(uploaded_csv)
            st.success(f"✅ Loaded {len(input_df):,} genes × {input_df.shape[1]} columns")
            st.dataframe(input_df.head(5), use_container_width=True)
        except Exception as e:
            st.error(f"Failed to read CSV: {e}")
            st.stop()

        # Validate all required feature columns are present
        feature_cols = model["feature_cols"]
        missing = [c for c in feature_cols if c not in input_df.columns]
        if missing:
            st.error(
                f"**{len(missing)} required feature column(s) missing from CSV:**\n\n"
                + ", ".join(missing[:15])
                + (" ..." if len(missing) > 15 else "")
            )
            st.stop()

        # ── Run stacking ensemble prediction ──────────────────────────────────
        with st.spinner("Running stacking ensemble…"):
            X_input  = input_df[feature_cols]
            svm_pred = model["svm_model"].predict(X_input)
            xgb_pred = model["xgb_base"].predict(X_input)
            stack_pred = model["meta"].predict(
                np.column_stack([svm_pred, xgb_pred])
            )

        # Replace negative predictions with random value between 0.01 and 0.03
        adjusted_pred = np.where(
            stack_pred < 0,
            np.random.uniform(0.001, 0.003, size=stack_pred.shape),
            stack_pred
            )

        result_df = pd.DataFrame({
            "Predicted gene expression log₂(FPKM + 1)": adjusted_pred.round(4),
            })

# ─────────────────────────────────────────────────────────────────────────────
# Results panel
# ─────────────────────────────────────────────────────────────────────────────
with col_results:
    if uploaded_csv is not None and "result_df" in locals():
        st.subheader(f"📊 Predictions — {selected_condition}")

        # Summary metrics
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Genes predicted", f"{len(result_df):,}")
        m2.metric("Mean log₂(FPKM + 1)",   f"{result_df['Predicted gene expression log₂(FPKM + 1)'].mean():.4f}")
        m3.metric("Min log₂(FPKM + 1)",    f"{result_df['Predicted gene expression log₂(FPKM + 1)'].min():.4f}")
        m4.metric("Max log₂(FPKM + 1)",    f"{result_df['Predicted gene expression log₂(FPKM + 1)'].max():.4f}")

        # Results table
        st.dataframe(result_df, use_container_width=True, height=380)

        # Chart
        st.subheader("Predicted Expression Distribution")
        chart_df = pd.DataFrame({
            "Predicted gene expression": sorted(adjusted_pred),
        })
        st.line_chart(chart_df, use_container_width=True)

        # Download
        st.subheader("⬇️ Download Results")
        cond_tag = selected_condition.split()[0]
        st.download_button(
            label="Download Predictions (CSV)",
            data=result_df.to_csv(index=True).encode("utf-8"),
            file_name=f"predictions_{cond_tag}.csv",
            mime="text/csv",
            icon=":material/download:",
        )

    elif uploaded_csv is None:
        st.info("⬅️ Upload a feature CSV on the left to see predictions here.")

# ─────────────────────────────────────────────────────────────────────────────
# Footer
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("")
st.markdown(
    "<div style='background-color:#32CD32; text-align:center'>"
    "<p style='color:white'>Copyright © 2026 ICAR-Indian Agricultural Statistics "
    "Research Institute, New Delhi-110012. All rights reserved.</p></div>",
    unsafe_allow_html=True,
)
