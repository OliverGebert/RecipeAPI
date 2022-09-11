from app import create_app, db
from models.recipe import Recipe
from models.user import User

# script to be run, in order to populate the db with user and recipes

app = create_app()

with app.app_context():

    user = User(username="Max", email="Max@arcor.de", password="oli")

    db.session.add(user)
    db.session.commit()

    pizza = Recipe(
        name="max pizza",
        description="lovely pizza",
        num_of_servings=2,
        cook_time=30,
        directions="easy",
        user_id=user.id,
    )

    db.session.add(pizza)
    db.session.commit()

    pasta = Recipe(
        name="max pasta",
        description="easy pasta",
        num_of_servings=4,
        cook_time=25,
        directions="easy preperation",
        user_id=user.id,
    )

    db.session.add(pasta)
    db.session.commit()
