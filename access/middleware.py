from .models import User
from django.http import HttpResponse, JsonResponse

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
			return JsonResponse({'message': 'Header api-key is missing'}, status = 401, safe = False)


	#Validates user via api key		
	def validate_user(self, key):
		try:
			u = User.objects.get(api_key=self.request.META[key])
		except User.DoesNotExist:
			return JsonResponse({'message': 'Invalid value for api-key'}, status = 401, safe = False)
		else:
			return self.validate_access(u)

	#Validates whether user has appropriate access
	def validate_access(self, u):
		if self.request.method == 'GET':
			return self.get_response(self.request)
		else:
			if not u.is_admin:
				return JsonResponse({'message': 'You do not have access to perform this action'}, status = 403, safe = False)
			else:
				return self.get_response(self.request)