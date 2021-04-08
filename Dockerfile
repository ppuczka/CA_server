ARG ver=3.8
FROM python:${ver} AS builder

LABEL author="ppuczka"
LABEL version="1.0.0"
LABEL date="2021-02-07"

COPY requirements.txt .

RUN pip install --user -r requirements.txt

FROM python:${ver}-slim

ARG baseDir="/app"

WORKDIR ${baseDir}
COPY . .
COPY --from=builder /root/.local /root/.local

EXPOSE 80

ENV PATH=/ppuczka/.local:$PATH

ENTRYPOINT [ "python" ]
CMD ["./ca_server_app.py"]