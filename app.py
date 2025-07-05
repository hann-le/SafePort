from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download")
def download():
    return send_from_directory(directory=os.path.join(app.root_path, 'static'),
                               path='SafePort.py', as_attachment=True)

@app.route("/downloadexe")
def downloadexe():
    return send_from_directory(directory=os.path.join(app.root_path, 'static'),
                               path='SafePort.exe', as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Use Render's dynamic port
    app.run(host="0.0.0.0", port=port)
