FROM nvidia/cuda:12.1.1-devel-ubuntu20.04

ENV PATH /opt/conda/bin:$PATH
RUN apt-get update && apt-get install -y \
    wget \
    git \
    curl \
    bzip2 \
    && wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh \
    && /bin/bash /tmp/miniconda.sh -b -p /opt/conda \
    && rm /tmp/miniconda.sh \
    && conda clean -afy

WORKDIR /app

COPY environment.yml ./

RUN conda env create -f environment.yml && conda clean -afy

COPY . /app/

SHELL ["conda", "run", "-n", "conda_venv", "/bin/bash", "-c"]

ENTRYPOINT ["conda", "run", "-n", "conda_venv", "python", "start.py"]
