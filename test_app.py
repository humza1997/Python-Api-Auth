import json
import pdb
from pprint import pprint

class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
     

    def test_get_recipes(self, api):
        res = api.get('/api/recipes')
        assert res.status == '200 OK'
        assert len(res.json) == 2

    def test_get_recipe(self, api):
        res = api.get('/api/recipes/2')
        assert res.status == '200 OK'
        assert res.json['Food_Name'] == 'Test Sauce'

    # def test_get_cats_error(self, api):
    #     res = api.get('/api/cats/4')
    #     assert res.status == '400 BAD REQUEST'
    #     assert "cat with id 4" in res.json['message']

    # def test_post_cats(self, api):
    #     mock_data = json.dumps({'name': 'Molly'})
    #     mock_headers = {'Content-Type': 'application/json'}
    #     res = api.post('/api/cats', data=mock_data, headers=mock_headers)
    #     assert res.json['id'] == 3

    # def test_patch_cat(self, api):
    #     mock_data = json.dumps({'name': 'Molly'})
    #     mock_headers = {'Content-Type': 'application/json'}
    #     res = api.patch('/api/cats/2', data=mock_data, headers=mock_headers)
    #     assert res.json['id'] == 2
    #     assert res.json['name'] == 'Molly'

    # def test_delete_cat(self, api):
    #     res = api.delete('/api/cats/1')
    #     assert res.status == '204 NO CONTENT'

    # def test_not_found(self, api):
    #     res = api.get('/bob')
    #     assert res.status == '404 NOT FOUND'
    #     assert 'Oops!' in res.json['message']