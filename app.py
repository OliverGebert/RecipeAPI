# from http import HTTPStatus

from flask import Flask  # , jsonify, request
from flask_restful import Api

from resources.recipe import RecipeListResource, RecipePublishResource, RecipeResource

app = Flask(__name__)
api = Api(app)

api.add_resource(RecipeListResource, "/recipes")
api.add_resource(RecipeResource, "/recipes/<int:recipe_id>")
api.add_resource(RecipePublishResource, "/recipes/<int:recipe_id>/publish")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
