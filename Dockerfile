FROM python:3.10

RUN mkdir /app
WORKDIR /app
COPY scai-eval24-metric-validator.py /app/

ENTRYPOINT [ "python3", "scai-eval24-metric-validator.py" ]
