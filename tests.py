import unittest, requests

class howtocity_api_tester(unittest.TestCase):
	
	def setUp(self):
		self.api_url = 'http://howtocity.herokuapp.com/api'

	def test_headers(self):
		r = requests.get(self.api_url+'/v1/categories')
		assert(r.headers['Access-Control-Allow-Origin']) == '*'
		assert(r.headers['Content-Type']) == 'application/json'

	def test_categories(self):
		r = requests.get(self.api_url+'/v1/categories')
		response = r.json()
		assert isinstance(response, dict)
		assert isinstance(response['objects'], list)
		assert isinstance(response['objects'][0]['id'], int)
		assert isinstance(response['objects'][0]['name'], unicode)
		assert isinstance(response['objects'][0]['description'], unicode)
		assert isinstance(response['objects'][0]['url'], unicode)
		assert isinstance(response['objects'][0]['lessons'], list)

	def test_lessons(self):
		r = requests.get(self.api_url+'/v1/lessons')
		response = r.json()
		assert isinstance(response, dict)
		assert isinstance(response['objects'], list)
		assert isinstance(response['objects'][0]['id'], int)
		assert isinstance(response['objects'][0]['name'], unicode)
		assert isinstance(response['objects'][0]['description'], unicode)
		assert isinstance(response['objects'][0]['url'], unicode)
		assert isinstance(response['objects'][0]['category_id'], int)
		assert isinstance(response['objects'][0]['category'], dict)

	def test_steps(self):
		r = requests.get(self.api_url+'/v1/steps')
		response = r.json()
		assert isinstance(response, dict)
		assert isinstance(response['objects'], list)
		assert isinstance(response['objects'][0]['id'], int)
		assert isinstance(response['objects'][0]['name'], unicode)
		assert isinstance(response['objects'][0]['step_type'], unicode)
		assert isinstance(response['objects'][0]['url'], unicode)
		assert isinstance(response['objects'][0]['lesson_id'], int)
		assert isinstance(response['objects'][0]['lesson'], dict)

	def test_admin(self):
		r = requests.get(self.api_url+'/admin')
		assert(r.headers['content-type']) == 'text/html; charset=utf-8'

if __name__ == '__main__':
	unittest.main()