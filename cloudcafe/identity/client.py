"""
This is an Identity Client
"""

import json
from cafe.engine.http.client import HTTPClient

class IdentityClient(HTTPClient):
	"""Identity Client Class for Rackspace"""
	def __init__(self, url, token):
		super(IdentityClient, self).__init__()
		self.url = url
		self.token = token
		self.default_headers = {
			"Accept": "application/json",
			"Content-Type": "application/json"}

	def authenticate(self, username, password):
		"""Authenticates with user and password and returns a response obj"""
		data = json.dumps({"auth": {"passwordCredentials": {
			"username": username, "password": password}}})
		url = "{url}/tokens".format(url=self.url)
		return self.post(url, data=data)

