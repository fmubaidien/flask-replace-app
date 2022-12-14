from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Deloitte, welcome to my test case\nPlease send raw string data to /replace and the response will contain the altered string'

@app.route('/replace', methods=['POST'])
def replace():
    words=["Google", "Microsoft", "Amazon" ,"Deloitte", "Oracle"]
    rep=request.data
    rep=rep.decode("utf-8")
    for i in words:
        rep=rep.replace(i, i+'©')
    return rep

if __name__ == "__main__":
    app.run(debug=True)