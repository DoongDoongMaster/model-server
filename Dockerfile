FROM python:3.11.5

# Install the necessary system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*
    
WORKDIR /home/code/automatic-drum-transcription

COPY ../automatic-drum-transcription/requirements.txt ./requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

WORKDIR /home/code/optical-music-recognition

COPY ../optical-music-recognition/requirements.txt ./requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

WORKDIR /home/code/model-server