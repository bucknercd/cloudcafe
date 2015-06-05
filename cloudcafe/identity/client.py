from cafe.engine.http.client import HTTPClient

class IdentityClient(HTTPClient):
	def __init__(self, url, token):
		super(IdentityClient, self).__init__()
		self.url = url
		self.token = token
		self.default_headers = {
			"Accept": "application/json",
			"Content-Type": "application/json"}

	