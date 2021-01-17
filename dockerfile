FROM python:3.8-slim
LABEL MAINTAINER xiaozhikang

COPY merge_yaml.py /app/merge_yaml.py
COPY entrypoint.sh /entrypoint.sh

RUN pip install --no-cache-dir PyYAML requests; \
    chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]