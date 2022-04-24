# FROM nvcr.io/nvidia/pytorch:21.07-py3
# FROM pytorch/pytorch:latest
FROM pytorch/pytorch:1.8.1-cuda11.1-cudnn8-runtime

RUN ln -fs /usr/share/zoneinfo/UTC /etc/localtime
RUN apt-get update && apt-get install -y \
    apt-utils \
    ffmpeg \
    libsm6 \
    libxext6 \
    libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Reqs
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
