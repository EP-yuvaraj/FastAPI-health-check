# FROM python:3.7.6

# COPY ./src /app/src

# COPY ./requirements.txt /app


# WORKDIR /app


# RUN pip install fastapi

# RUN pip install uvicorn

# RUN pip freeze > requirements.txt


# RUN pip install -r requirements.txt



# EXPOSE 7000

# # HEALTHCHECK --interval=5s --timeout=3s --retries=3 CMD curl -f / https://thormarketdata.extrapreneursindia.com/fastapi-test:7000 || exit 1

# CMD ["uvicorn" ,"src.main:app","--host=0.0.0.0","--port=7000","--reload"]


FROM python:3.7.6


COPY ./ /app
WORKDIR /app
RUN pip install -r requirements.txt 
EXPOSE 9001
CMD ["python","main.py"]