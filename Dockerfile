# app/Dockerfile

FROM python:3.10-slim

EXPOSE 7860

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    poppler-utils\
    && rm -rf /var/lib/apt/lists/*

# RUN git clone https://github.com/streamlit/streamlit-example.git .

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]