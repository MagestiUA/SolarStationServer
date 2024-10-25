FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
RUN pip install gunicorn
EXPOSE 5001
CMD ["gunicorn", "SolarStationServer.wsgi:application", "--bind", "0.0.0.0:5001", "--workers", "3"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]