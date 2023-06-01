import importlib
try:
    importlib.import_module('flask')
except ImportError:
    import subprocess
    subprocess.call(['pip', 'install', 'flask'])
finally:
    from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inner')
def inner():
    return render_template('inner-page.html')

@app.route('/details')
def details():
    return render_template('portfolio-details.html')


if __name__ == '__main__':
    app.run()
    