FROM python:3.12

COPY .deployment/requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /app

CMD [ "/app/.deployment/start.sh" ]