
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download")
def download():
    # Serve the securiscan.py script for download
    return send_from_directory(directory=os.path.join(app.root_path, 'static'),
                               path='SafePort.py', as_attachment=True)

@app.route("/downloadexe")
def downloadexe():
    # Placeholder: serve securiscan.exe if you build it and put it in static folder
    return send_from_directory(directory=os.path.join(app.root_path, 'static'),
                               path='SafePort.exe', as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
