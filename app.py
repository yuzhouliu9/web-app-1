from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'web-app-1: /'

@app.route('/developer')
def developer():
    return 'web-app-1: /developer'

@app.route('/developer/sub/path')
def developer():
    return 'web-app-1: /developer/sub/path'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
