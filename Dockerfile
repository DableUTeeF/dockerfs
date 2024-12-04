FROM nvcr.io/nvidia/pytorch:21.05-py3 
RUN apt-get update
RUN apt-get install zsh
RUN sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"

RUN conda create --name openmmlab python=3.8 -y
RUN conda activate openmmlab

WORKDIR /work
COPY . .
RUN pip install -r requirements.txt

RUN pip install -U openmim
RUN mim install mmengine
RUN mim install "mmcv>=2.0.0rc4,<2.2.0"

RUN git clone https://github.com/open-mmlab/mmdetection.git
RUN cd mmdetection
RUN pip install -v -e .
