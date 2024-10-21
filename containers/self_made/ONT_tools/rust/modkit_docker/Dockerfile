#Bootstrap: docker
FROM ubuntu:20.04

#%labels
LABEL Maintainer="samuel ahuno"
#    Version v0.0.1

#%help
#    Singularity for rust and cargo

#%post
    # Install dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    autoconf \
    automake \
    build-essential \
    bzip2 \
    gcc wget curl git
#RUN pip install pod5
    ### add rust and cargo

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

#SHELL PATH="/root/.cargo/bin:${PATH}"

#ENV PATH="/root/.cargo/bin:${PATH}"

#RUN bash -c "source ~/.cargo/env"
#RUN export PATH="$HOME/.cargo/bin/cargo:$PATH"    
#RUN echo '$(ls -thal .)'
#RUN ls -thal /usr/local/bin

RUN bash -c 'source /root/.cargo/env'

RUN cargo --help
#RUN ~/.cargo/bin/cargo --help

#RUN ~/.cargo/bin/cargo --help
 
#install modkit
RUN git clone https://github.com/nanoporetech/modkit.git
RUN cd modkit
RUN cargo install --path .
    
#move cargo binaries to /usr/local/
#RUN mv /root/.cargo /usr/local/.cargo && ls -thal /usr/local/.cargo/bin && ln -s  /usr/local/.cargo/bin/* /usr/local/bin/
    
#%environment
#ENV PATH="/usr/local/bin:$PATH"
ENV LISTEN_PORT=12345
#ENV PATH="/usr/local/.cargo/bin:$PATH"
#ENV PATH="/root/.cargo/bin:${PATH}"
#%runscript
CMD ["bash", "-c", "echo 'this is docker for modkit' && exec \"$@\"" ] 
#echo "This is a Singularity container for modkit which depends on rust Cargo"
#    exec "$@"

#%test
    # Test if softwares are installed correctly
#RUN cargo --version
#RUN rustc --version
#RUN modkit --version
