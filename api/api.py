from flask import Flask

# API imports:
from lib.api_v1 import apiBlueprint

app = Flask(__name__)
app.register_blueprint(apiBlueprint, url_prefix='/v1')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
