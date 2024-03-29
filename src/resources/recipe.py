from http import HTTPStatus

from flask import request
from flask_restful import Resource
from models.recipe import Recipe, recipe_list


class RecipeListResource(Resource):
    def get(self):

        data = []

        for recipe in recipe_list:
            if recipe.is_published is True:
                data.append(recipe.data)

        return {"data": data}, HTTPStatus.OK

    def post(self):
        json_data = request.get_json()

        name = json_data.get("name")
        description = json_data.get("description")
        num_of_servings = json_data.get("num_of_servings")
        cook_time = json_data.get("cook_time")
        directions = json_data.get("directions")

        recipe = Recipe(
            name=name,
            description=description,
            num_of_servings=num_of_servings,
            cook_time=cook_time,
            directions=directions,
        )
        recipe.save()
        data = {"name": recipe.name}

        return data, HTTPStatus.CREATED


class RecipeResource(Resource):
    def get(self, recipe_id):

        recipe = next(
            (
                recipe
                for recipe in recipe_list
                if recipe.id == recipe_id and recipe.is_published is True
            ),
            None,
        )

        if recipe is None:
            return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND

        return recipe.data, HTTPStatus.OK

    def put(self, recipe_id):
        data = request.get_json()

        recipe = next(
            (recipe for recipe in recipe_list if recipe.id == recipe_id), None
        )

        if recipe is None:
            return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND

        recipe.name = data["name"]
        recipe.description = data["description"]
        recipe.num_of_servings = data["num_of_servings"]
        recipe.cook_time = data["cook_time"]
        recipe.directions = data["directions"]

        return recipe.data, HTTPStatus.OK

    def delete(self, recipe_id):
        # deletes recipe even if not published

        recipe = next(
            (recipe for recipe in recipe_list if recipe.id == recipe_id),
            None,
        )

        if recipe is None:
            return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND
        else:
            recipe_list.remove(recipe)

        return recipe.data, HTTPStatus.OK


class RecipePublishResource(Resource):
    def put(self, recipe_id):
        recipe = next(
            (recipe for recipe in recipe_list if recipe.id == recipe_id), None
        )

        if recipe is None:
            return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND

        recipe.is_published = True

        return {}, HTTPStatus.NO_CONTENT

    def delete(self, recipe_id):
        recipe = next(
            (recipe for recipe in recipe_list if recipe.id == recipe_id), None
        )

        if recipe is None:
            return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND

        recipe.is_published = False

        return {}, HTTPStatus.NO_CONTENT
