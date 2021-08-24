import pytest
import app
from controllers import recipes

@pytest.fixture
def api(monkeypatch):
    test_recipes = [
    {'id': 1, 'Food_Name': 'Test Wings', 'Ingredients': ['Test Raw Chicken Wings','Oil'], 'Instructions': '1)Test the wings!'},
 {'id': 2, 'Food_Name': 'Test Sauce', 'Ingredients': ['Test Sauce','Oil'], 'Instructions': '1)Test the sauce!'}  
]

    monkeypatch.setattr(recipes, "recipes", test_recipes)
    api = app.app.test_client()
    return api