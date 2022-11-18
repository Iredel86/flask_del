import json
from flask import Flask
# from flaskgit init


app = Flask(__name__)
# CORS(apps)

ar = [{"name":"ido","age":"36"},{"name":"haim","age":"37"},{"name":"kuki","age":"27"}]
@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/data')
def hello():
    return ar
 
 
if __name__ == '__main__':
    app.run(debug=True)