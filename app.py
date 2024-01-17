from flask import Flask, request, session
import subprocess, socket

app = Flask(__name__)
app.secret_key = 'woa.dlc.wp23'

@app.route('/', methods = ['POST'])
def get():
    subprocess.Popen('python3 stress_cpu.py', shell=True)
    return 'success'

@app.route('/', methods = ['GET'])
def set():
    return socket.gethostname()

if __name__ == '__main__':
    app.run(host="0.0.0.0")

