from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', 
        status="Build Passing",
        branch="main",
        last_run="2 minutes ago",
        commit="9f3a2b1",
        tests_passed=42
    )

@app.route('/health')
def health():
    return {"status": "Healthy", "version": "3.11.7", "coverage": "92%"}

if __name__ == '__main__':
    app.run(debug=True)
