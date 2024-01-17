from flask import Flask, request, session
app = Flask(__name__)
app.secret_key = 'woa.dlc.wp23'

@app.route('/', methods = ['GET'])
def get():
    if session.get('num') != None:
        return session['num']
    else:
        return '100'


@app.route('/', methods = ['POST'])
def set():
    session['num'] = request.json['num']
    return 'success'

if __name__ == '__main__':
    app.run(host="0.0.0.0")
