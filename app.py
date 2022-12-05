from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Deloitte, welcome to my test case'

@app.route('/test', methods=['POST'])
def replace():
    words=["Google", "Microsoft", "Amazon" ,"-+Deloitte", "Oracle"]
    rep=request.data
    rep=rep.decode("utf-8")
    for i in words:
        rep=rep.replace(i, i+'©')
    return rep