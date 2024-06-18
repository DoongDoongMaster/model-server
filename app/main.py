import io
import cv2
import logging
import sys, os
import xml.etree.ElementTree as ET

from fastapi import FastAPI, File, UploadFile

# 2 계층 위의 상위 폴더 접근
sys.path.append(f'{os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))}/automatic-drum-transcription/src')
# sys.path.append(f'{os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))}/optical-music-recognition/ddm-omr')
print(sys.path)

from constant import (
    SAMPLE_RATE,
    SERVED_MODEL_ALL,
)
from feature.feature_extractor import FeatureExtractor
from serving.model_serving import ModelServing
import infer

app = FastAPI()
# 로그 생성
logger = logging.getLogger()
# 로그의 출력 기준 설정
logger.setLevel(logging.INFO)


curr_model_num = 1
data = SERVED_MODEL_ALL[curr_model_num]
model_serving_class = ModelServing(
    data.get("method_type"),
    data.get("feature_type"),
    data.get("model_name"),
    data.get("label_cnt"),
)


@app.post("/adt/predict", tags=["ADT"])
def model_predict(file: bytes = File(...)):
    logger.info("[ADT] I recived API server POST request")
    # ============ sercved model class create ========================

    logger.info("[ADT] I'm waiting model prediction")
    # # Implement model predict logic
    bytesIO = io.BytesIO(file)
    audio = FeatureExtractor.load_audio(bytesIO)
    drum_instrument, onsets_arr = model_serving_class.predict_model_from_server(audio)
    logger.info("model prediction done !!!")

    # total wav file time (sec)
    audio_total_sec = len(audio) / SAMPLE_RATE

    return {
        "drum_instrument": drum_instrument,
        "onsets_arr": onsets_arr,
        "audio_total_sec": audio_total_sec,
    }

# 저장할 디렉토리 경로 설정
UPLOAD_DIRECTORY = "./uploaded_files/"

# 디렉토리가 존재하지 않으면 생성
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


@app.post("/omr/predict", tags=["OMR"])
async def omr_predict(file: UploadFile = File(...)):
    logger.info("[OMR] I recived API server POST request")
    # ============ sercved model class create ========================

    try:
        # 업로드된 파일의 이름을 가져옴
        filename = file.filename
        
        # 파일 저장 경로 설정
        file_location = os.path.join(UPLOAD_DIRECTORY, filename)

        # 파일 저장
        with open(file_location, "wb") as f:
            f.write(await file.read())

        img = cv2.imread(file_location, cv2.IMREAD_UNCHANGED)
        print(img)
        
        tree = infer.inference(img)

        # BytesIO 객체를 사용하여 XML 트리를 바이트 데이터로 변환
        byte_io = io.BytesIO()
        tree.write(byte_io, encoding="utf-8", xml_declaration=True)

        # 바이트 데이터를 가져옴
        byte_data = byte_io.getvalue()

        return {"result": byte_data}
    
    except Exception as e:
        return {"error": str(e)}