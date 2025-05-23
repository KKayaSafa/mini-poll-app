import os
import mysql.connector
from flask import Flask, request, render_template_string
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

app = Flask(__name__)

QUESTIONS = [
    "Bu projeyi faydalı buldum.",
    "Docker kullanımı kolaydı.",
    "Flask ile çalışmak keyifliydi.",
    "Veritabanı bağlantısı zorlayıcıydı.",
    "Docker Compose mantığını anladım.",
    "Ortam değişkenleri yönetilebilir.",
    "Kod yapısı sade ve anlaşılır.",
    "Geliştirme ortamını kolay kurdum.",
    "Test etmek basitti.",
    "Bu teknolojileri tekrar kullanırım."
]

FORM_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Survey</title>
    <style>
      :root {
        --bg-color: #f9f9f9;
        --text-color: #222;
        --card-bg: #fff;
        --button-bg: #007bff;
        --button-color: #fff;
      }
      body.dark-mode {
        --bg-color: #121212;
        --text-color: #e0e0e0;
        --card-bg: #1e1e1e;
        --button-bg: #444;
        --button-color: #fff;
      }

      body {
        background-color: var(--bg-color);
        color: var(--text-color);
        font-family: 'Segoe UI', sans-serif;
        margin: 0;
        padding: 0;
        transition: background-color 0.3s ease, color 0.3s ease;
      }

      .container {
        max-width: 800px;
        margin: auto;
        padding: 30px;
      }

      h1 {
        text-align: center;
        margin-bottom: 30px;
      }

      .question {
        background-color: var(--card-bg);
        padding: 20px;
        margin-bottom: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
      }

      label {
        margin-right: 20px;
      }

      button, .dark-toggle {
        background-color: var(--button-bg);
        color: var(--button-color);
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 20px;
      }

      .dark-toggle {
        float: right;
      }

      .message {
        margin-top: 20px;
        text-align: center;
        font-weight: bold;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <button class="dark-toggle" onclick="toggleDarkMode()">🌙</button>
      <h1>Açık Kaynaklı Yazılımlar Dersi Proje Değerlendirme Anketi</h1>
      <form method="POST">
        {% for question in questions %}
          <div class="question">
            <p><strong>{{ loop.index }}. {{ question }}</strong></p>
            <label><input type="radio" name="q{{ loop.index0 }}" value="agree" required> Katılıyorum</label>
            <label><input type="radio" name="q{{ loop.index0 }}" value="neutral"> Kararsızım</label>
            <label><input type="radio" name="q{{ loop.index0 }}" value="disagree"> Katılmıyorum</label>
          </div>
        {% endfor %}
        <button type="submit">Gönder</button>
      </form>
      {% if submitted %}
        <div class="message">Teşekkürler! Cevaplarınız kaydedildi.</div>
      {% endif %}
    </div>

    <script>
      function toggleDarkMode() {
        document.body.classList.toggle('dark-mode');
      }
    </script>
  </body>
</html>
"""


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )

@app.route("/", methods=["GET", "POST"])
def survey():
    submitted = False
    if request.method == "POST":
        answers = [request.form.get(f"q{i}") for i in range(10)]
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO poll_responses
                (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, answers)
            conn.commit()
            cursor.close()
            conn.close()
            submitted = True
        except Exception as e:
            print("Hata:", e)
    return render_template_string(FORM_TEMPLATE, questions=QUESTIONS, submitted=submitted)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
