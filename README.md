# Model server
> 모델을 서빙하는 서버

## API Docs
### 1. POST `/adt/predict`
- ADT 모델의 예측 요청을 보내는 API

### 2. POST `/omr/predict`
- OMR 모델의 예측 요청을 보내는 API

<br>

## Preparation
- clone ADT & OMR repository
  - [ADT repo](https://github.com/DoongDoongMaster/automatic-drum-transcription)
  - [OMR repo](https://github.com/DoongDoongMaster/optical-music-recognition)
  - ‼️ 주의 : 아래와 같이 폴더 구조를 맞춰야 합니다.
    ```shell
    ...
    ├── model-server
    ├── automatic-drum-transcription
    ├── optical-music-recognition
    ```

- install docker engine
  ```shell
  # Add Docker's official GPG key:
  sudo apt-get update
  sudo apt-get install ca-certificates curl
  sudo install -m 0755 -d /etc/apt/keyrings
  sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
  sudo chmod a+r /etc/apt/keyrings/docker.asc
  
  # Add the repository to Apt sources:
  echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  sudo apt-get update

  sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
  ```
- install docker compose
  ```shell
  sudo apt-get update
  sudo apt-get install docker-compose-plugin
  ```
<br>

## Run
- 서버 실행 명령어
  <br>
  
  ```shell
  docker compose up --build
  ```

- 로컬 호스트에서 docs 확인
  ```
  localhost:5000/docs
  ```
