
FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app/
RUN pip3 install --no-cache-dir -r req.txt
EXPOSE 8080
CMD ["python", "app.py"]
