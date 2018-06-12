from .models import User
from django.http import HttpResponse

class CheckUser:

	def __init__(self, get_response):
		self.get_response = get_response

	#This method checks api key and accordingly grants access to requesting users	
	def __call__(self, request):
		self.request = request
		key = 'HTTP_API_KEY'
		if key in self.request.META:
			return self.validate_user(key)
		else:
			return HttpResponse('Header api-key is missing')


	#Validates user via api key		
	def validate_user(self, key):
		try:
			u = User.objects.get(api_key=self.request.META[key])
		except User.DoesNotExist:
			return HttpResponse('Invalid value for api-key')
		else:
			return self.validate_access(u)

	#Validates whether user has appropriate access
	def validate_access(self, u):
		if self.request.method == 'GET':
			return self.get_response(self.request)
		else:
			if not u.is_admin:
				return HttpResponse('You do not have access to perform this action')
			else:
				return self.get_response(self.request)