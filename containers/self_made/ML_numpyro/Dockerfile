##ML & numpyro-ppl (probablistic programming) 

# Add labels
#LABEL maintainer="samuel ahuno" version="v0.0.1"

#how to build and push to dockerub
#1. build image
# docker build -t numpyroml .

#2. tag:
# docker tag <image_ID> sahuno/<image_name>:[tag]

#how to run
# option1: run jupyterlab
# docker run -p 8888:8888 -v $(pwd):/workspace numpyroml jupyter

# option 2: run bash
# docker run -it -v $(pwd):/workspace numpyroml bash
      
FROM nvcr.io/nvidia/jax:25.01-py3
RUN python --version
RUN pip3 --version
RUN pip install numpyro jupyterlab

RUN pip install "arviz[all]"
RUN pip install seaborn
RUN ls -thal
# Set up workspace
RUN mkdir -p /workspace
WORKDIR /workspace

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8888

ENTRYPOINT ["/entrypoint.sh"]
