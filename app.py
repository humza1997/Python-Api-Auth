from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import recipes
from werkzeug import exceptions
import pdb
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
CORS(app)
auth = HTTPBasicAuth()

users = {
    "humza": generate_password_hash("chicken"),
    "shav": generate_password_hash("wing"),
    "scott": generate_password_hash("sauce")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/')
@auth.login_required
def home():
    return f'Welcome to the Chicken Wing Factory {auth.current_user()}! ', 200

@app.route('/api/recipes', methods=['GET', 'POST'])
@auth.login_required
def recipes_handler():

    fns = {
        'GET': recipes.index,
        'POST': recipes.create
    }
    new_recipe = request.get_json()
    resp, code = fns[request.method](request)
    if request.method == 'POST':
        return f'You have added a recipe for {new_recipe["Food_Name"]}', code
    else :
        return jsonify(resp), code

@app.route('/api/recipes/<int:recipe_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
@auth.login_required
def recipe_handler(recipe_id):
    fns = {
        'GET': recipes.show,
        'PATCH': recipes.update,
        'PUT': recipes.update,
        'DELETE': recipes.destroy
    }
    resp, code = fns[request.method](request, recipe_id)
    return jsonify(resp), code

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return '<img src="https://media.giphy.com/media/1dOLvKVcmKZ0YXJAKw/giphy.gif?cid=ecf05e47c1xe974j7ilqsd265k0irxw906rsbs7ubksc9cgf&rid=giphy.gif&ct=g"> <br> <br> <h1>NO CHICKENS HERE!</h1>', 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500

if __name__ == "__main__":
    app.run(debug=True)
