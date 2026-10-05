FROM python:3
ADD app/ /app
WORKDIR /app
RUN apt-get update
RUN pip install -r requirements.txt
RUN useradd -m -r appuser && chown -R appuser:appuser /app
USER appuser
CMD python app.py