FROM python:3.9-slim


COPY ./src /app/src
COPY ./requirements.txt /app
RUN mkdir -p /app/database

WORKDIR /app

RUN pip3 install -r requirements.txt
#RUN python3 sqliteCreatTables 

WORKDIR /app/src

EXPOSE 8000
CMD ["uvicorn", "photos:app", "--host=0.0.0.0", "--reload"] 

