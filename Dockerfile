#
# 개발 상태의 Django 프로젝트를 컨테이너를 사용해서 배포하기 위한 이미지.
# 

# 베이스 이미지: 2026년 표준 Python 3.14 slim 버전 사용.
FROM python:3.14-slim

# 작업폴더 설정.
# 이후 "." 은 이 작업폴더를 의미한다.
WORKDIR /usr/src/app

# 환경변수 설정: .pyc 파일 생성하지 않도록 함.
ENV PYTHONDONTWRITEBYTECODE=1

# 환경변수 설정: 파이썬 로그가 버퍼링 없이 즉각 출력되도록 한다.
ENV PYTHONUNBUFFERED=1

# requirements.txt를 작업폴더로 들여온다. (먼저 복사)
COPY requirements.txt .

# 파이썬 환경 구성.
# --no-cache-dir 옵션을 사용해서 임시 파일을 남지기 않으므로 이미지 용량 축소에 도움이 된다.
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 폴더 내용을 작업폴더로 복사. (나머지 복사)
COPY . .
