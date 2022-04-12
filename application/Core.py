from wsgiref.util import request_uri
import requests
import http.cookiejar

def show_cookie(self):
		if len(self.value) > 100:
			i = 0
			value = ''
			while i < len(self.value):
				value += (self.value[i:i+100] + '\n')
				i += 100
		else:
			value = self.value
		return ("Name: %s Domain: %s Secure: %s Path: '%s' Version: %s Port: %s\nValue: %s" % (self.name, self.value, self.secure, self.path, self.version, self.port, self.value))

http.cookiejar.Cookie.__str__ = show_cookie

class User():
	def __init__(self):
		self.cookies = []
		self.requests = []
		self.session = requests.Session()

	def add_cookie(self, name, value, domain, secure,
		path = '/',
		version = 0, 
		port = None, 
		expires = None, 
		discard = None, 
		comment = None, 
		comment_url = None, 
		rest = {'HttpOnly': None}, 
		rfc2109 = False):

		if path == "":
			path = '/'

		if comment == "":
			comment = None

		try:
			version = int(version)
		except:
			version = 0

		try:
			port = int(port)
		except:
			port = None
		
		required_args = {
		'name': name,
		'value': value
		}

		optional_args = {
		'version': version,
		'port': port,
		'domain': domain,
		'path': path,
		'secure': secure,
		'expires': expires,
		'discard': discard,
		'comment': comment,
		'comment_url': comment_url,
		'rest': rest,
		'rfc2109': rfc2109
		}

		cookie = requests.cookies.create_cookie(**required_args, **optional_args)
		self.cookies.append(cookie)

	def add_request(self, type, url, verify):
		self.requests.append(Request(type, url, verify))

	def send(self, request):
		if request.type == "GET":
			return self.session.get(request.url, verify=request.verify)
		elif request.type == "POST":
			return self.session.get(request.url, verify=request.verify)
		elif request.type == "DELETE":
			return self.session.get(request.url, verify=request.verify)


class SourcePortAdapter(requests.adapters.HTTPAdapter):
    """"Transport adapter" that allows us to set the source port."""
    def __init__(self, port, *args, **kwargs):
        self._source_port = port
        super(SourcePortAdapter, self).__init__(*args, **kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = requests.packages.urllib3.poolmanager.PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, source_address=('', self._source_port))

class Request():
	def __init__(self, request_type, url, verify):
		self.type = request_type
		self.url = url
		self.verify = verify




