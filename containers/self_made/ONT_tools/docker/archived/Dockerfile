# Use Ubuntu 20.04 as the base image
FROM ubuntu:20.04

# Add labels
LABEL maintainer="samuel ahuno" \
      version="v0.0.1"

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies (note cmake is included)
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    autoconf \
    automake \
    bzip2 \
    gcc \
    git \
    make \
    wget \
    curl \
    ca-certificates \
    build-essential \
    libncurses-dev \
    libbz2-dev \
    liblzma-dev \
    libdeflate-dev \
    libcrypto++-dev \
    cmake && \
    rm -rf /var/lib/apt/lists/*

# (Optional) Create a "python" symlink so that "python" points to python3
RUN ln -s /usr/bin/python3 /usr/bin/python

# Set working directory to /opt
WORKDIR /opt

# ----------------------------------------------------------------------------
# Install Rust (rustc and cargo)
# ----------------------------------------------------------------------------
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y 

# Ensure Cargo is on the PATH for subsequent commands
ENV PATH="/root/.cargo/bin:${PATH}"

# ----------------------------------------------------------------------------
# Limit parallelism and reduce memory usage during Cargo builds
# ----------------------------------------------------------------------------
# ENV CARGO_BUILD_JOBS=1
# ENV MALLOC_ARENA_MAX=2

# ----------------------------------------------------------------------------
# Now install pod5 (which needs Rust/Cargo for building its Rust extensions)
# ----------------------------------------------------------------------------
RUN pip3 install pod5

# ----------------------------------------------------------------------------
# Install Oxford Nanopore basecaller Dorado
# ----------------------------------------------------------------------------
RUN wget https://cdn.oxfordnanoportal.com/software/analysis/dorado-0.9.1-linux-x64.tar.gz && \
    tar -xvzf dorado-0.9.1-linux-x64.tar.gz && \
    mv dorado-0.9.1-linux-x64 /usr/local/dorado && \
    ln -s /usr/local/dorado/bin/dorado /usr/local/bin/dorado && \
    rm dorado-0.9.1-linux-x64.tar.gz

# ----------------------------------------------------------------------------
# Install modkit using cargo
# ----------------------------------------------------------------------------
RUN git clone https://github.com/nanoporetech/modkit.git && \
    cd modkit && \
    cargo install --path . && \
    cd .. && rm -rf modkit

# ----------------------------------------------------------------------------
# Install Samtools
# ----------------------------------------------------------------------------
RUN wget https://github.com/samtools/samtools/releases/download/1.21/samtools-1.21.tar.bz2 && \
    tar -xvjf samtools-1.21.tar.bz2 && \
    cd samtools-1.21 && \
    ./configure --prefix=/usr/local && \
    make && \
    make install && \
    cd .. && \
    rm -rf samtools-1.21 samtools-1.21.tar.bz2

# ----------------------------------------------------------------------------
# Install pycoQC via pip
# ----------------------------------------------------------------------------
RUN pip3 install pycoQC


# ----------------------------------------------------------------------------
# Install longphase for phasing methylation
# ----------------------------------------------------------------------------
RUN wget https://github.com/twolinin/longphase/releases/download/v1.7.3/longphase_linux-x64.tar.xz && \
    tar -xJf longphase_linux-x64.tar.xz && \
    mv longphase_linux-x64 /usr/local/bin/longphase && \
    chmod +x /usr/local/bin/longphase && \
    rm longphase_linux-x64.tar.xz

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
# RUN wget https://cdn.oxfordnanoportal.com/software/analysis/dorado-0.9.1-linux-x64.tar.gz && \
#     tar -xvzf dorado-0.9.1-linux-x64.tar.gz && \
#     mv dorado-0.9.1-linux-x64 /usr/local/dorado && \
#     ln -s /usr/local/dorado/bin/dorado /usr/local/bin/dorado && \
#     rm dorado-0.9.1-linux-x64.tar.gz

# # ----------------------------------------------------------------------------
# # Create an entrypoint script to mimic the Singularity %runscript behavior
# # ----------------------------------------------------------------------------
# RUN echo '#!/bin/sh' > /entrypoint.sh && \
#     echo 'echo "This is a Docker container for Samtools, Oxford Nanopore basecaller Dorado, Python, and Rust."' >> /entrypoint.sh && \
#     echo 'exec "$@"' >> /entrypoint.sh && \
#     chmod +x /entrypoint.sh

# ENTRYPOINT ["/entrypoint.sh"]
# CMD ["bash"]

