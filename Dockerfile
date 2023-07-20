
FROM python:3.9-slim
WORKDIR /app
COPY app.py app_utils.py index.html result.html style.css requirements.txt ./
RUN pip install --no-cache-dir -r req.txt
EXPOSE 8080
CMD ["python", "app.py"]

