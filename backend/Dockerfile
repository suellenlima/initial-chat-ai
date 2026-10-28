# 1) Base Python Image
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 2) Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/* 

# 3) Create a no-root user
RUN addgroup --system app \
    && adduser --system --ingroup app app

# 4) Set work directory
WORKDIR /app

# 5) Install Python dependencies
COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel \
    && pip install --prefer-binary --no-cache-dir -r requirements.txt

# 6) Copy project files
COPY app /app/app

# 7) Change ownership of the app directory
RUN chown -R app:app /app

# 8) Switch to the no-root user
USER app

# 9) Expose the port the app runs on
EXPOSE 8000

# 10) Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
