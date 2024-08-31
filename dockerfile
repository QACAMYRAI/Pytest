FROM python:3.9-slim

WORKDIR /pytestdemo

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

COPY start.sh .

RUN chmod +x start.sh

ENTRYPOINT ["./start.sh"]
