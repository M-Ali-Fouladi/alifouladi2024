FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install Flask gunicorn
EXPOSE 5000

ENV CONFIG_VALUE="defaultConfig"
ENV SECRET_VALUE="defaultSecret"
ENV ENV_VALUE="defaultEnv"

# Run app.py when the container launches
#CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
#CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:5000", "--timeout", "120", "app:app"]
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

