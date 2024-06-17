#!/bin/sh

# ADT model serving
cd automatic-drum-transcription/src/
python run_model_serving.py

exec "$@"