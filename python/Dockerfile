FROM python:3.7-alpine

ARG project_dir=/app

WORKDIR ${project_dir}

COPY ./src ${project_dir}

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

CMD ["python", "app.py"]