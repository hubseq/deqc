# Use miniconda image base from Dockerhub
FROM continuumio/miniconda3

# Metadata
LABEL container.base.image = "miniconda3:python3.9"
# # Use Python image base from Dockerhub
#FROM python:3.7
# LABEL container.base.image = "python:3.7"
LABEL software.name = "deqc"

# Install system packages and AWS CLI
RUN apt-get -y update && \
    apt-get -y install python3-pip
RUN pip install awscli boto3
RUN conda install -c anaconda pandas
RUN conda install -c anaconda numpy
RUN conda install -c anaconda scipy
RUN conda install -c anaconda scikit-learn
RUN conda install -c plotly plotly
RUN conda install -c conda-forge python-kaleido
RUN conda install -c conda-forge matplotlib

WORKDIR /

# copy relevant scripts to root dir
RUN mkdir -p global_utils/src
COPY src/run_main.py /
COPY src/run_program.py /
COPY src/deqc.py /
COPY src/global_utils/src/module_utils.py /global_utils/src/
COPY src/global_utils/src/file_utils.py /global_utils/src/
COPY src/global_utils/src/global_keys.py /global_utils/src/
COPY src/global_utils/src/aws_s3_utils.py /global_utils/src/
ENV PATH="/usr/local/bin/:$PATH"

ENTRYPOINT ["python","/run_main.py"] 
