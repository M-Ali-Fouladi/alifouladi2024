FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install Flask gunicorn
EXPOSE 8080
ENV NAME World
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
