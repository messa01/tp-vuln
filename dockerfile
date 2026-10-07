FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --upgrade msgpack setuptools urllib3
RUN pip uninstall -y pip setuptools wheel

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
