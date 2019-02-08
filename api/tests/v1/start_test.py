from  api import create_app

import unittest
"""super test for all test"""
class Start(unittest.TestCase):

	def setUp(self):
		self.app = create_app('testing')
		self.client = self.app.test_client()
		self.item_list = []

	def tearDown(self):
		self.app=None
		del self.item_list







