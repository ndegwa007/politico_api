from .start_test import Start
from api.v1.views.view_parties import parties

'''test for all view_parties endpoints'''
class TestParties(Start):


	def setUp(self):
		'''set up objects required for this test'''
		super(TestParties,self).setUp()

		self.just_aparty = {
			"name": 'Jubilee',
			"hq_address": 'Kisumu',
			"logo_url": 'url',
			"slogan": 'tuko pamoja'
		}
		'''clear parties list after test'''
	def tearDown(self):
		super(TestParties,self).tearDown()
		del parties[:]

		'''testing post a party'''
	def test_create_party(self):

		res = self.client.post("api/v1/parties", json=self.just_aparty)
		data = res.get_json()

		self.assertEqual(data['status'],201)
		self.assertEqual(data['message'], 'Party created successfully')
		self.assertEqual(res.status_code, 201)