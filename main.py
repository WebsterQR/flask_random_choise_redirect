import random
from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def main():
    redirect_url = random.choice(seq=["https://icdsgroup.ru/lendgc", "https://icdsgroup.ru/bizonlend"])
    return redirect(redirect_url, code=302)

if __name__ == "__main__":
    app.run(port=3000)