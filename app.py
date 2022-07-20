from flask import Flask
app = Flask(__name__)

#test

@app.route('/')
def index():
    return 'another app: /'

@app.route('/developer-another-app', strict_slashes=False) # matches with trailing /
def developer():
    return 'another app: /developer-another-app'

@app.route('/developer-another-app/sub/path', strict_slashes=False)
def developer2():
    return 'another app: /developer-another-app/sub/path'

@app.route('/developer/another-app', strict_slashes=False)
def developer3():
    return 'another app: /developer/another-app'

@app.route('/developer/another-app/sub/path', strict_slashes=False)
def developer4():
    return 'another app: /developer/another-app/sub/path'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
