FROM python:3.8-slim-buster
USER root
RUN mkdir /app
COPY . /app
WORKDIR /app/

RUN apt-get update && apt-get install -y build-essential python3-dev libffi-dev libbz2-dev liblzma-dev
RUN pip install --upgrade pip setuptools wheel
RUN pip3 install -r requirements.txt
ENV AIRFLOW_CORE_DAGBAG_IMPORT_TIMEOUT=1000
ENV AIRFLOW_CORE_ENABLE_XCOM_PICKLING=t=True
RUN airflow db init
RUN airflow users create -e rishiberi17988@gmail.com -f kshitij -l beri -p admin -r Admin -u admin
RUN chmod 777 start.sh
RUN apt update -y

ENTRYPOINT [ "/bin/sh" ]
CMD ["python3", "app.py"]
