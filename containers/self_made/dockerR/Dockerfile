# Step 1: import official R base image
# FROM rocker/r-ver
FROM rocker/rstudio
# FROM bioconductor/bioconductor_docker:devel
#FROM rocker/rstudio
# docker build -t sahuno/rdocker:1.1 .


#step 1: create dir to work
# Make a directory for your project (optional)
RUN mkdir -p /dockerR_dir/data/processed /dockerR_dir/data/raw /dockerR_dir/data/preprocessed /dockerR_dir/figures /dockerR_dir/reports /dockerR_dir/scripts

# Set working directory
WORKDIR /dockerR_dir

#Step 2: copy the R packages table file into the Docker image

# Set the maintainer label
LABEL maintainer="ekwame001@gmail.com"

#Step 2a(optional): # Set environment variables
# ENV LANG=C.UTF-8 LC_ALL=C.UTF-8


#Step 3: option 2: install R packages from a file
RUN R -e "print('Hello World')"
# RUN R -e "pkgs <- read.delim('/dockerR_dir/data/raw/minimal_packages_to_install.csv', header=TRUE,sep = ","); pkgs$Core_CRAN; message(pkgs$Core_CRAN); \
# install_cran.lib <- pkgs$Core_CRAN[!pkgs$Core_CRAN %in% installed.packages()]; install.packages(pkgs$Core_CRAN, dependencies=TRUE,ask = FALSE)"

RUN R -e 'if (!require("BiocManager", quietly = TRUE)) install.packages("BiocManager")'
RUN R -e 'BiocManager::install(c("DESeq2", "EnhancedVolcano", "plyranges","GenomicRanges" ,"BSgenome",\
"biomaRt", "Biostrings", "genomation", "bsseqData", "BSgenome.Mmusculus.UCSC.mm10", "bsseq", \
"org.Hs.eg.db", "ChIPseeker", "DOSE", "TxDb.Hsapiens.UCSC.hg38.knownGene", "rtracklayer", "ChIPseeker", \
"SummarizedExperiment", "clusterProfiler","org.Mm.eg.db", "AnnotationDbi", "GO.db", "GOstats", "GenomicFeatures", "Biostrings", "ComplexHeatmap", "Rsubread", ""),ask = F)'

RUN R -e 'BiocManager::install(c("methylKit", "edgeR"), ask = F)'
RUN R -e  'install.packages(c("janitor", "fst"), dependencies=TRUE,ask = FALSE)'

# install system deps needed by devtools/remotes
RUN apt-get update && apt-get install -y \
      libcurl4-openssl-dev \
      libssl-dev \
      libxml2-dev \
      git \
    && rm -rf /var/lib/apt/lists/*

# install.packages("devtools")
RUN R -e 'install.packages(c("devtools","remotes"), dependencies=TRUE, repos="http://cran.rstudio.com/")'
#RUN R -e 'install.packages(c("devtools","remotes"), dependencies=TRUE, repos="http://cran.rstudio.com/");library(devtools);devtools::install_github("fstPackage/fst", ref = "develop")'
RUN R -e 'remotes::install_github("fstPackage/fst", ref = "develop")'
RUN R -e 'remotes::install_github("mskilab/gUtils")'
RUN R -e 'if (!require("remotes", quietly=TRUE)) install.packages("remotes", repos="http://cran.rstudio.com/"); remotes::install_github("nicolerg/ssGSEA2")'
RUN R -e 'install.packages(c("optparse","entropy","factoextra","ggbiplot","RColorBrewer", "cowplot", "NbClust", "ggnewscale", "ggfortify", "ggrepel", "pheatmap", "magrittr", "viridis", "data.table", "pak", "tidyplots", "circlize"), dependencies=TRUE, ask = FALSE)'


