FROM python:3.11.5

WORKDIR /home/code/automatic-drum-transcription

COPY ../automatic-drum-transcription/requirements.txt ./requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt


WORKDIR /home/code