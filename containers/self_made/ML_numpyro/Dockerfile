##ML & numpyro-ppl (probablistic programming) 

# Add labels
#LABEL maintainer="samuel ahuno" version="v0.0.1"

#how to run
#1. build image
# docker build -t numpyroml .

#2. tag:
# docker tag <image_ID> sahuno/<image_name>:[tag]
      
FROM nvcr.io/nvidia/jax:25.01-py3
RUN python --version
RUN pip3 --version
RUN pip install numpyro

RUN pip install "arviz[all]"
RUN pip install seaborn
