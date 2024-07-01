FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y \
    apt-utils \
    curl \
    python3 \
    python3-pip \
    git \
    libgl1-mesa-glx \
    libglib2.0-0 \
    build-essential \
    g++ \
    cmake \
    tzdata && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set timezone
RUN ln -fs /usr/share/zoneinfo/Etc/UTC /etc/localtime && dpkg-reconfigure --frontend noninteractive tzdata

RUN pip3 install --upgrade pip

RUN git clone https://github.com/open-mmlab/mmaction2.git
RUN pip3 install numpy
RUN pip3 install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118
RUN pip3 install openmim
RUN mim install mmengine
RUN mim install mmcv==2.0.0
RUN mim install mmdet
RUN mim install mmpose
WORKDIR mmaction2

RUN pip3 install -v -e .

COPY . .

ENTRYPOINT ["python3", "main.py"]
CMD ["--input_video", "h2YqqUhnR34.mp4"]