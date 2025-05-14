#############################
# Dockerfile for Transcript Annotation
# Multi-arch: linux/amd64 and linux/arm64
#############################

# Use Miniconda base image
FROM --platform=${BUILDPLATFORM:-linux/amd64} continuumio/miniconda3:latest

LABEL maintainer="Your Name <you@example.com>"

# Prevent prompts
ENV DEBIAN_FRONTEND=noninteractive

# Add Bioconda and Conda-Forge channels
RUN conda config --add channels defaults \
    && conda config --add channels bioconda \
    && conda config --add channels conda-forge \
    && conda config --set channel_priority strict

# Create environment and install tools
RUN conda install -y \
        python=3.9 \
        gffcompare \
        gffread \
        sqanti3 \
        transdecoder \
        hmmer \
        blast \
        r-base \
        r-essentials \
        bioconductor-clusterprofiler \
    && conda clean -afy

# Install additional R/Bioconductor dependencies via BiocManager
RUN R -e "if (!requireNamespace('BiocManager', quietly=TRUE)) install.packages('BiocManager', repos='https://cloud.r-project.org'); BiocManager::install(c('AnnotationDbi','org.Hs.eg.db'))"

# Set PATH for conda
ENV PATH="/opt/conda/bin:$PATH"

# Create working directory
WORKDIR /data

# Default entrypoint
ENTRYPOINT ["bash"]
