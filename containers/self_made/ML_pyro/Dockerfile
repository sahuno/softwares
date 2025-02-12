##ML with probablistic programming 
#how to run 
# docker build -t pyroml .

#run with docker
# docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 -it sahuno/pyroml jupyter

#run with singulairty (assumiing you've already pulled container)
# singularity run --nv --bind /data1/greenbab/:/workspace pyroml.sif jupyter


FROM nvcr.io/nvidia/pytorch:25.01-py3
RUN python --version
RUN pip3 --version

RUN  pip3 install pyro-ppl jupyterlab

#install additional stats tools
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
#author: samuel ahuno
#date: Feb 11 2025
