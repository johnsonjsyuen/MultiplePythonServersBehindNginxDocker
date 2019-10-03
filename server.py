import os
from flask import Flask
app = Flask(__name__)

MACHINE_ID = os.environ['MACHINE_ID']
PORT = int(os.environ['PORT'])

@app.route('/')
def hello_world():
    return f'Hello, World! This is server:{MACHINE_ID}'

if __name__ == '__main__':
    app.run( host="0.0.0.0", port = PORT)
