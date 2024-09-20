from controllers.lenguajecontroller import BlueprintLenguaje
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(BlueprintLenguaje)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)