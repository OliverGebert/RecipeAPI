from app import create_app, db
from models.recipe import Recipe
from models.user import User

app = create_app()

with app.app_context():

    user = User.query.filter_by(username="oli").first()
    for recipe in user.recipes:
        print(
            "{} recipe made by {} can serve {} people.".format(
                recipe.name, recipe.user.username, recipe.num_of_servings
            )
        )
