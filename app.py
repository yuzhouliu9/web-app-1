from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'main app: /'

@app.route('/developer', strict_slashes=False) # matches /developer and /developer/
def developer():
    return 'main app: /developer'

@app.route('/developer/sub/path', strict_slashes=False) # matches with trailing /
def developer_sub_path():
    return 'main app: /developer/sub/path'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
