''' Recipe controller '''
from werkzeug.exceptions import BadRequest

recipes = [
    {'id': 1, 'Food_Name': 'Plain Wings', 'Ingredients': ['Raw Chicken Wings',['Flour, Paprika, Salt, Pepper, Secret Ingredient 1, Secret Ingredient 2, Secret Ingredient 3'], 'Oil'], 'Instructions': '1)Coat the raw chicken in dry batter. 2)Preheat oil to 170 deg C. 3)Place coated wings in fry basket, drop basket in oil. 4)Leave to cook for minimum 8 minutes.'},
    {'id': 2, 'Food_Name': 'Korean BBQ Sauce', 'Ingredients': ['Gochujang', 'Soy Sauce', 'Secret Ingredient 4', 'Secret Ingredient 5'], 'Instructions': '1)Mix that ****'},
  {'id': 3, 'Food_Name': 'Lemon Pepper Seasoning', 'Ingredients': ['Lemon', 'Pepper', 'Butter'], 'Instructions': '1)Toss them wings with the ingredients.'}
]

def index(req):
    return [r for r in recipes], 200

def show(req, uid):
    return find_by_uid(uid), 200

def create(req):
    new_recipe = req.get_json()
    new_recipe['id'] = sorted([r['id'] for r in recipes])[-1] + 1
    recipes.append(new_recipe)
    return new_recipe, 201

def update(req, uid):
    recipe = find_by_uid(uid)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        recipe[key] = val
    return recipe, 200

def destroy(req, uid):
    recipe = find_by_uid(uid)
    recipes.remove(recipe)
    return recipe, 204

def find_by_uid(uid):
    try:
        return next(recipe for recipe in recipes if recipe['id'] == uid)
    except:
        raise BadRequest(f"We don't have that recipe with id {uid}!")