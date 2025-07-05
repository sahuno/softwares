# Use rocker/tidyverse as the base image, which includes R, RStudio, and the Tidyverse suite.
#FROM rocker/tidyverse:4.3.2
FROM bioconductor/bioconductor_docker:devel

# Define metadata for the image
LABEL Author="Sam Ahuno" \
      Version="2.0" \
      Description="R container with a comprehensive set of packages for genomic data analysis, including DMR annotation."

# Set environment variables
ENV R_VERSION=4.3.2 \
    LC_ALL=C \
    LANG=C

# ------------------------------------------------------------------
# Install all system dependencies in a single layer
# ------------------------------------------------------------------
RUN apt-get update && apt-get install -y \
    # Dependencies for various R packages
    libgsl-dev \
    libhdf5-dev \
    libmariadb-dev \
    libpq-dev \
    libsqlite3-dev \
    tcl8.6-dev \
    tk8.6-dev \
    pandoc \
    cmake \
    # Dependencies for devtools, remotes, and git-based installs
    git \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    && rm -rf /var/lib/apt/lists/*

# ------------------------------------------------------------------
# Install BiocManager and devtools first
# ------------------------------------------------------------------
RUN R -e 'install.packages("BiocManager", repos="https://cloud.r-project.org")' && \
    R -e 'install.packages(c("devtools", "remotes"), repos="https://cloud.r-project.org")'

# ------------------------------------------------------------------
# Install methylKit early to catch any issues
# ------------------------------------------------------------------
RUN R -e "library(devtools); install_github('al2na/methylKit', build_vignettes=FALSE, repos=BiocManager::repositories(), ref='development', dependencies=TRUE)"

# ------------------------------------------------------------------
# Install remaining R packages
# ------------------------------------------------------------------
RUN R -e "install.packages(c( \
        'data.table', 'tidyverse', 'cowplot', 'ggrepel', 'ggnewscale', \
        'ggpubr', 'GGally', 'pheatmap', 'RColorBrewer', 'viridis', 'viridisLite', \
        'circlize', 'cola', 'ComplexUpset', 'UpSetR', 'factoextra', 'NbClust', \
        'pvclust', 'entropy', 'janitor', 'knitr', 'optparse', 'svglite', 'fst', \
        'openxlsx', 'crayon', 'rlist', 'msigdbr', 'ggfortify', 'ggbiplot', \
        'tidyplots', 'magrittr', 'pak' \
    ), repos='https://cloud.r-project.org')" && \
    \
    # Install a consolidated list of Bioconductor packages
    R -e "BiocManager::install(c( \
        'GenomicRanges', 'S4Vectors', 'IRanges', 'BiocGenerics', 'rtracklayer', \
        'AnnotationDbi', 'GenomicFeatures', 'AnnotationHub', \
        'regioneR', 'org.Hs.eg.db', 'org.Mm.eg.db', \
        'TxDb.Hsapiens.UCSC.hg19.knownGene', 'TxDb.Hsapiens.UCSC.hg38.knownGene', \
        'TxDb.Mmusculus.UCSC.mm10.knownGene', 'ChIPseeker', 'clusterProfiler', \
        'DESeq2', 'edgeR', 'DOSE', 'EnhancedVolcano', 'ComplexHeatmap', 'GSVA', \
        'plyranges', 'BSgenome', 'biomaRt', 'Biostrings', 'genomation', \
        'bsseqData', 'BSgenome.Mmusculus.UCSC.mm10', 'bsseq', \
        'SummarizedExperiment', 'GO.db', 'GOstats', 'Rsubread' \
    ), update=FALSE, ask=FALSE)" && \
    \
    # Install packages from GitHub using the 'remotes' package
    R -e "remotes::install_github('fstPackage/fst', ref = 'develop')" && \
    R -e "remotes::install_github('mskilab/gUtils')" && \
    R -e "remotes::install_github('nicolerg/ssGSEA2')" && \
    R -e "devtools::install_github('rcavalcante/annotatr')" && \
    \
    # Clean up temporary files to reduce image size
    rm -rf /tmp/*

# ------------------------------------------------------------------
# Finalization
# ------------------------------------------------------------------

# Verify that key packages can be loaded successfully
RUN R -e "library(GenomicRanges); library(tidyverse); library(DESeq2); library(methylKit)"

# Set the entrypoint to R, making the container executable as the R interpreter
ENTRYPOINT ["R"]

# Provide a default command (--help) to show R's help message if run without arguments
CMD ["--help"]
