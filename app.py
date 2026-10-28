from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', last_run="2 minutes ago", commit="9f3a2b1", tests_passed=42)

@app.route('/health')
def health():
    return {"status": "Healthy"}

if __name__ == '__main__':
    app.run()
