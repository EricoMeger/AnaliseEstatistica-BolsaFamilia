FROM python:3.10-slim

WORKDIR /app

COPY /csv ./csv
COPY /modules ./modules
COPY /images ./images
COPY requirements.txt ./
COPY main.py ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
