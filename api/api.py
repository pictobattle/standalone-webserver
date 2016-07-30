from flask import Flask

# API imports:
from lib.api_v1 import APIv1

app = Flask(__name__)
apiv1 = APIv1(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
