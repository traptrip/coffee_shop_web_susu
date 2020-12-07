FROM python:3.8-slim

COPY . .
RUN pip install -r requirements.txt
#CMD ["python", "app.py"]
CMD gunicorn -w 4 --bind 0.0.0.0:${PORT} app:app
