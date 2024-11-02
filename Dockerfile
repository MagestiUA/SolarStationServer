FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
RUN mkdir -p /app/staticfiles /app/mediafiles
RUN python manage.py collectstatic --noinput
RUN useradd -m appuser && chown -R appuser /app
USER appuser
RUN pip install gunicorn
EXPOSE 8000
CMD ["gunicorn", "SolarStationServer.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
