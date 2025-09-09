from flask import Blueprint, render_template, request
from .sample_data import recipes

main = Blueprint('main', __name__)

@main.route('/')
def index():
    query = request.args.get('q', '').lower()
    filtered = [r for r in recipes if query in r['title'].lower()] if query else recipes
    return render_template('index.html', recipes=filtered)

@main.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    return render_template('recipe_detail.html', recipe=recipe)

@main.route('/add')
def add_recipe():
    return render_template('add_recipe.html')
