from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from catalogues.models import Movie
from django.forms.models import model_to_dict
from django.db.models import Q
import json

# Lists all the movies present
def index(request):
	movies = list(Movie.objects.values())
	return JsonResponse({'data':movies}, status = 200, safe = False)

# Adds a new movie only via an admin
def create(request):
	body_json = json.loads(request.body)
	print(body_json)
	valid = validate_request(body_json)
	if not valid:
		return JsonResponse({'message': 'Incomplete/incorrect request'}, status = 400, safe = False)
	else:
		valid = sanitize_data(request)
		Movie.objects.create(name=body_json['name'], director=body_json['director'], imdb_score=body_json['imdb_score'], popularity=body_json['popularity'], genres=body_json['genres'])
		return JsonResponse({'data': 'Record successfully created'}, status = 200, safe = False)

# Checks for all required fields to create a movie record
def validate_request(body_json):
	valid = True
	# Check if even one field is missing
	if 'name' not in body_json or 'imdb_score' not in body_json or 'director' not in body_json or 'popularity' not in body_json or 'genres' not in body_json:
		valid = False

	# Check if even one field is null or empty
	elif not body_json['name'] or not body_json['imdb_score'] or not body_json['director'] or not body_json['genres'] or not body_json['popularity']:
		valid = False

	# Check if values are empty strings
	elif not body_json['name'].strip() or not body_json['director'].strip() or not body_json['genres'].strip():
		valid = False

	# Check if not floating numbers	

	return valid

def sanitize_data(request):
	valid = True
	#Formatting genres to store correctly
	return valid

# Returns a specific movie record
def edit(request, id):
	try:
		m = Movie.objects.get(id=id)
		return JsonResponse({'data': model_to_dict(m)}, status = 200, safe = False)
	except Movie.DoesNotExist:
		return JsonResponse({'message': 'No such movie exists'}, status = 400, safe = False)

# Updates a particular movie record
def update(request, id):
	body_json = json.loads(request.body)
	valid = validate_request(body_json)
	if not valid:
		return JsonResponse({'message': 'Incomplete request'}, status = 400, safe = False)
	else:
		valid = sanitize_data(request)
		m = Movie.objects.filter(id=id).update(name=body_json['name'], director=body_json['director'], imdb_score=body_json['imdb_score'], popularity=body_json['popularity'], genres=body_json['genres'])		
		if not m:
			return JsonResponse({'message': 'No such movie exists'}, status = 400, safe = False)
		else:
			return JsonResponse({'data': body_json}, status = 200, safe = False)

# Removes a particular movie record
def delete(request, id):
	try:
		Movie.objects.filter(id=id).delete()
		return JsonResponse({'message': 'Movie deleted successfully'}, status = 200, safe = False)
	except Movie.DoesNotExist:
		return JsonResponse({'message': 'No such movie exists'}, status = 400, safe = False)

# Searches for a movie based on 'q' query parameter
def search(request):
	if 'q' not in request.GET:
		return JsonResponse({'message': 'No search query present'}, status = 400, safe = False)
	else:
		search = request.GET['q']
		results = list(Movie.objects.filter(Q(name__icontains=search) | Q(director__icontains=search) | Q(genres__icontains=search)).values())
		return JsonResponse({'data': results}, status = 200, safe = False)	
					