FROM python:3.10

WORKDIR /redisapi

COPY /requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENV PORT=8001

EXPOSE 8001

CMD [ "uvicorn", "publisher:app","--host","0.0.0.0","--reload" ]