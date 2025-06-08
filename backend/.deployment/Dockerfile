FROM python:3.12

COPY .deployment/requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /app

# TODO change to run on supervisord when have celery service
CMD ["gunicorn", "config.wsgi:application", "--workers", "3", "--bind", "0.0.0.0:8000"]