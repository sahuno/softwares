# Use official Python 3.12 slim image as base (includes Python 3.12 and pip)
FROM python:3.12-slim
ARG TARGETOS
ARG TARGETARCH

# Expose build-time variables for multi-arch builds
ENV TARGETOS=${TARGETOS} \
    TARGETARCH=${TARGETARCH}

#FROM public.ecr.aws/docker/library/ubuntu:20.04

# Add labels
LABEL maintainer="samuel ahuno" \
      version="v0.0.1"

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive
# Instruct openssl-sys to use system OpenSSL rather than vendoring
ENV OPENSSL_NO_VENDOR=1

## Install OS-level dependencies (cmake, compilers, bioinformatics tools)
RUN apt-get update && apt-get install -y --no-install-recommends \
    autoconf \
    automake \
    bzip2 \
    tabix \
    bedtools \
    bcftools \
    vcftools \
    samtools \
    python3-dev \
    gffread \
    libboost-all-dev \
    zlib1g-dev \
    gcc \
    git \
    make \
    wget \
    curl \
    ca-certificates \
    build-essential \
    pkg-config \
    libssl-dev \
    libncurses-dev \
    libbz2-dev \
    liblzma-dev \
    libdeflate-dev \
    libcrypto++-dev \
    cmake && \
    rm -rf /var/lib/apt/lists/*


# Set working directory to /opt
WORKDIR /opt

# ----------------------------------------------------------------------------
# Install Rust (rustc and cargo)
# ----------------------------------------------------------------------------
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y 

# Ensure Cargo is on the PATH for subsequent commands
ENV PATH="/root/.cargo/bin:${PATH}"

# ----------------------------------------------------------------------------
# Install modkit using cargo
# ----------------------------------------------------------------------------
RUN git clone https://github.com/nanoporetech/modkit.git && \
    cd modkit && \
    cargo install --path . && \
    cd .. && rm -rf modkit && \
    chmod +x /root/.cargo/bin/modkit


# grab latest stable tag (change to a commit/tag if you want a fixed version)
#RUN git clone --depth 1 https://github.com/samtools/htslib.git /src/htslib && \
#    cd /src/htslib && autoheader && autoconf && \
#    ./configure --enable-libcurl --enable-libdeflate && \
#    make -j$(nproc)

# ----------------------------------------------------------------------------
# Limit parallelism and reduce memory usage during Cargo builds
# ----------------------------------------------------------------------------
# ENV CARGO_BUILD_JOBS=1
# ENV MALLOC_ARENA_MAX=2


# ----------------------------------------------------------------------------
# Install Oxford Nanopore basecaller Dorado (amd64 only)
# ----------------------------------------------------------------------------
RUN if [ "${TARGETARCH}" = "amd64" ] ; then \
    wget https://cdn.oxfordnanoportal.com/software/analysis/dorado-0.9.6-linux-x64.tar.gz && \
    tar -xvzf dorado-0.9.6-linux-x64.tar.gz && \
    mv dorado-0.9.6-linux-x64 /usr/local/dorado && \
    ln -s /usr/local/dorado/bin/dorado /usr/local/bin/dorado && \
    rm dorado-0.9.6-linux-x64.tar.gz ; \
  else \
    echo "Skipping Dorado installation for architecture ${TARGETARCH}" ; \
  fi


## Samtools installed via apt (no need to build from source)

# ----------------------------------------------------------------------------
# Install pycoQC and additional python packages via pip
# ----------------------------------------------------------------------------
RUN pip3 install \
    pycoQC \
    deeptools \
    methylartist \
    nanoplot \
    seaborn \
    matplotlib \
    pandas \
    numpy \
    cyvcf2 \
    git+https://github.com/fritzsedlazeck/Sniffles.git

## Sniffles and gffread installed via pip and apt, no manual build needed

# ----------------------------------------------------------------------------
# Install UCSC Kent utilities for amd64 only via rsync (avoids broken tgz)
RUN if [ "${TARGETARCH}" = "amd64" ] ; then \
    apt-get update && apt-get install -y --no-install-recommends rsync && \
    mkdir -p /usr/local/kent && \
    rsync -aP rsync://hgdownload.soe.ucsc.edu/genome/admin/exe/linux.x86_64/ /usr/local/kent/ && \
    # Copy all executables (including in subdirectories) to /usr/local/bin
    find /usr/local/kent -type f -perm /111 -exec cp {} /usr/local/bin/ \; && \
    rm -rf /usr/local/kent && \
    apt-get remove -y rsync && apt-get autoremove -y && rm -rf /var/lib/apt/lists/* ; \
  else \
    echo "Skipping UCSC Kent utilities for architecture ${TARGETARCH}" ; \
  fi
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Install longphase for phasing methylation (amd64 only)
# ----------------------------------------------------------------------------
RUN if [ "${TARGETARCH}" = "amd64" ] ; then \
    wget https://github.com/twolinin/longphase/releases/download/v1.7.3/longphase_linux-x64.tar.xz && \
    tar -xJf longphase_linux-x64.tar.xz && \
    mv longphase_linux-x64 /usr/local/bin/longphase && \
    chmod +x /usr/local/bin/longphase && \
    rm longphase_linux-x64.tar.xz ; \
  else \
    echo "Skipping longphase installation for architecture ${TARGETARCH}" ; \
  fi

# ----------------------------------------------------------------------------
# Create an entrypoint script to mimic the Singularity %runscript behavior
# ----------------------------------------------------------------------------
RUN echo '#!/bin/sh' > /entrypoint.sh && \
    echo 'echo "This is a Docker container for Samtools, Oxford Nanopore basecaller Dorado, Python, and Rust."' >> /entrypoint.sh && \
    echo 'exec "$@"' >> /entrypoint.sh && \
    chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash"]

# # Use Ubuntu 20.04 as the base image
# FROM ubuntu:20.04

# # docker build -t onttools .
# # docker builder prune -a
# # Add labels similar to the Singularity %labels section
# LABEL maintainer="samuel ahuno" \
#       version="v0.0.1"

# # Avoid interactive prompts during package installation
# ENV DEBIAN_FRONTEND=noninteractive

# # Install dependencies
# RUN apt-get update && apt-get install -y \
#     python3 \
#     python3-pip \
#     autoconf \
#     automake \
#     bzip2 \
#     gcc \
#     git \
#     make \
#     cmake \
#     wget \
#     curl \
#     ca-certificates \
#     build-essential \
#     libncurses-dev \
#     libbz2-dev \
#     liblzma-dev \
#     libdeflate-dev \
#     libcrypto++-dev && \
#     rm -rf /var/lib/apt/lists/*

# # (Optional) Create a "python" symlink so that "python" points to python3
# RUN ln -s /usr/bin/python3 /usr/bin/python

# # Set working directory to /opt for the following installations
# WORKDIR /opt

# # ----------------------------------------------------------------------------
# # Install Rust (rustc and cargo) early so that pip3 can use Cargo when needed
# # ----------------------------------------------------------------------------
# RUN curl https://sh.rustup.rs -sSf | sh -s -- -y 

# # Ensure Cargo is on the PATH for subsequent commands
# ENV PATH="/root/.cargo/bin:${PATH}"

# # ----------------------------------------------------------------------------
# # Now install pod5 (which needs Rust/Cargo for building its Rust extensions)
# # ----------------------------------------------------------------------------
# RUN pip3 install pod5


# # ----------------------------------------------------------------------------
# # Install Oxford Nanopore basecaller Dorado
# # ----------------------------------------------------------------------------
# RUN wget https://cdn.oxfordnanoportal.com/software/analysis/dorado-0.9.6-linux-x64.tar.gz && \
#     tar -xvzf dorado-0.9.6-linux-x64.tar.gz && \
#     mv dorado-0.9.6-linux-x64 /usr/local/dorado && \
#     ln -s /usr/local/dorado/bin/dorado /usr/local/bin/dorado && \
#     rm dorado-0.9.6-linux-x64.tar.gz

# # ----------------------------------------------------------------------------
# # Create an entrypoint script to mimic the Singularity %runscript behavior
# # ----------------------------------------------------------------------------
# RUN echo '#!/bin/sh' > /entrypoint.sh && \
#     echo 'echo "This is a Docker container for Samtools, Oxford Nanopore basecaller Dorado, Python, and Rust."' >> /entrypoint.sh && \
#     echo 'exec "$@"' >> /entrypoint.sh && \
#     chmod +x /entrypoint.sh

# ENTRYPOINT ["/entrypoint.sh"]
# CMD ["bash"]

