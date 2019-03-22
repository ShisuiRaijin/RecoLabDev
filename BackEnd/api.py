from flask import Flask
from flask_restful import Api
from BackEnd.router.Router import Router


app = Flask(__name__)
api = Api(app)
router = Router(api)

if __name__ == '__main__':
    app.run(debug=True)
