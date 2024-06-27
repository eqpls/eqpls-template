FROM python:3.12.4-alpine3.20
RUN pip install --no-cache-dir fastapi uvicorn asyncio aiohttp aiofiles aiopath websockets python-multipart stringcase requests luqum psycopg[binary,pool] elasticsearch redis
RUN mkdir -p /opt/module
WORKDIR /opt/module
ENTRYPOINT ["python", "server"]