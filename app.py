import json
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
# CORS(apps)

ar = [{"name":"ido","age":"36"},{"name":"haim","age":"37"},{"name":"kuki","age":"27"}]
@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/data')
def data():
     return json.dumps(ar)
 
 
if __name__ == '__main__':
    app.run(debug=True)
 