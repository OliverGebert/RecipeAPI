# RecipeAPI

## Purpose

Simple Flask application which defines URL endpoints, binds to a postgres DB for storage

## Architecture

for Details on the architecture visit /Documentation/Architecture.md
To generate .png files from .drawio, use *make all*

## Documentation

within the documentation folder, there is a Makefile with target all and clean to generate .png files for arkdown or delete them.

## Testing

Unit testing is implemented with pytest: run pytest from top project folder

integration testing of API and database is done via postman. please run newman locally with Recipes.postman_collection.json