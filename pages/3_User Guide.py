import streamlit as st
import os

# ─────────────────────────────────────────────────────────────────────────────
# Header
# ─────────────────────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns([1.5, 20, 2])
with col1:
    st.image("static/images/icarlogo.png", width=150)
with col2:
    st.markdown("<h1 style='text-align:center;'>EpiStackXpress: Epigenetic Stacking Ensemble for Gene eXpression</h1>", unsafe_allow_html=True)
with col3:
    st.image("static/images/iasri-logo.png", width=150)

st.markdown("---")
st.header("📖 User Guide")
st.markdown("<p style='text-align:justify;'>Follow the steps below to prepare your input features for EpiStackXpress. Download the provided scripts at the relevant steps to automate the process.</p>", unsafe_allow_html=True)
st.markdown("---")


# Step 1

st.subheader("🖌 Step 1: Obtain gene annotations")
st.markdown("<p style='text-align:justify;'>The GFF3 annotation file should be obtained from a reliable public database such as NCBI, EMBL, or DDBJ. In this workflow, gene prediction is performed using AUGUSTUS (DOI: 10.1093/nar/gkh379), and the subsequent commands have been standardized according to the AUGUSTUS-based annotation procedure.</p>", unsafe_allow_html=True)

st.markdown("**Commands:**")
st.code("augustus --species=<species_name> genome.fa > augustus_predictions.gff", language="bash")


st.markdown("---")


# Step 2 — with downloadable script

st.subheader("🖌 Step 2: Generate methylation calls")
st.markdown("<p style='text-align:justify;'>Bi-Sulphite sequences should be downloaded from any repository and go through the pipeline of bismark (DOI: 10.1093/bioinformatics/btr167) tool</p>", unsafe_allow_html=True)

st.markdown("**Commands:**")
st.code("Genome Preparation: bismark_genome_preparation --bowtie2 /path/to/genome_directory/", language="bash")
st.code("Alignment: bismark --genome /path/to/genome_directory/ -1 sample_R1.fastq.gz -2 sample_R2.fastq.gz -o bismark_output/", language="bash")
st.code("Deduplication: deduplicate_bismark --paired bismark_output/sample_R1_bismark_bt2_pe.bam", language="bash")
st.code("Generate CX report, coverage, and bedGraph together: bismark_methylation_extractor --paired-end --bedGraph --cutoff <User-defined > --CX bismark_output/sample_R1_bismark_bt2_pe.deduplicated.bam", language="bash")

st.markdown("---")

# Step 3
st.subheader("🖌 Step 3: Count methylated sites per region")
st.markdown("<p style='text-align:justify;'>The methylated cytosines should be counted for further analysis. Use the recommended following code (e.g., 3-4 hours for Rice), which needs high computational power for using Spark. Change the configuration of Spark as per local device. One can do without Spark also which is time-consuming (e.g., around 4-5 Days). Promoter length is user-defined and crop-specifc. But all Promoter length should remain constant. Total 15 csv files will be generated for features and two csv will denote the protein sequence, generated from each gene. </p>", unsafe_allow_html=True)

st.markdown("**Instructions:**")
st.info("Use Computer having high computational power facility")
# Download script for Step 3
script3 = "static/scripts/GFF_Bismark_Spark.py"
if os.path.exists(script3):
    with open(script3, "rb") as f:
        st.download_button(
            label="⬇️ Download Script for Step 3",
            data=f,
            file_name="GFF_Bismark_Spark.py",
            mime="text/x-python",
            icon=":material/download:",
        )
else:
    st.info("Place your script at: `static/scripts/GFF_Bismark_Spark.py`")
st.markdown("---")

# ─────────────────────────────────────────────────────────────────────────────
# Step 4 — with downloadable script
# ─────────────────────────────────────────────────────────────────────────────
st.subheader("🖌 Step 4: Normalize by region length")
st.markdown("<p style='text-align:justify;'>The range of methylation count, varies widely. That should be normalised using respective length.</p>", unsafe_allow_html=True)

st.markdown("**Instructions:**")
st.info("Store all csv files in one folder of local device and run the following python based code for merging all csv and calculating normalised value")

# Download script for Step 4
script4 = "static/scripts/Feature_normalisation.py"
if os.path.exists(script4):
    with open(script4, "rb") as f:
        st.download_button(
            label="⬇️ Download Script for Step 4",
            data=f,
            file_name="Feature_normalisation.py",
            mime="text/x-python",
            icon=":material/download:",
        )
else:
    st.info("Place your script at: `static/scripts/Feature_normalisation.py`")

st.markdown("---")

# ─────────────────────────────────────────────────────────────────────────────
# Step 5 — with downloadable script
# ─────────────────────────────────────────────────────────────────────────────
st.subheader("🖌 Step 5: Calculate genomic features")
st.markdown("<p style='text-align:justify;'>Calculate GC, Tetra-nucleotide frequency formula and use standardscaler for normalising tetra-nucleotide frequencies.</p>", unsafe_allow_html=True)

st.markdown("**Instructions:**")
st.info("Take 2kb Upstream and 2kb downstream sequence around TSS for genomic prediction")
st.markdown("---")

# ─────────────────────────────────────────────────────────────────────────────
# Step 6 — with downloadable script
# ─────────────────────────────────────────────────────────────────────────────
st.subheader("🖌 Step 6: Merge features")
st.markdown("<p style='text-align:justify;'>Merge genomic features with the epigenetic features in the recommended order described in sample csv. Then Ultimately, 272 features should be uploaded in server for gene prediction</p>", unsafe_allow_html=True)

st.markdown("**Destination:**")
st.info("Enjoy! Now Ready to use.")
st.markdown("---")

# ─────────────────────────────────────────────────────────────────────────────
# Footer
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("")
st.markdown("<div style='background-color:#32CD32; text-align:center'><p style='color:white'>Copyright © 2026 ICAR-Indian Agricultural Statistics Research Institute, New Delhi-110012. All rights reserved.</p></div>", unsafe_allow_html=True)
