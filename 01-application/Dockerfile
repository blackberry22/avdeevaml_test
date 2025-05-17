FROM python:3.10.17-alpine3.21
ENV AUTHOR_NAME=avdeeva_ml
RUN mkdir -p /home/app
WORKDIR /home/app 
COPY test.py /home/app 
EXPOSE 8000
CMD ["python", "test.py"]

