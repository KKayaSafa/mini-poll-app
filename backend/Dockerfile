# Temel Python imajını kullan
FROM python:3.12-slim

# Ortam değişkeni: stdout'a log yazmak için
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Çalışma dizini oluştur
WORKDIR /app

# Gerekli dosyaları kopyala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Flask uygulamasını başlat
CMD ["flask", "run", "--host=0.0.0.0"]
