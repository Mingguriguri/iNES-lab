# 베이스 이미지 설정 (Python 3.12을 사용)
FROM python:3.12-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요 파일들을 작업 디렉토리로 복사
COPY . /app

# 필요한 패키지 설치
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 애플리케이션 실행 (애플리케이션에 따라 수정 필요)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
