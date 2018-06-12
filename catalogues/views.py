from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from catalogues.models import Movie
from django.forms.models import model_to_dict
from django.db.models import Q
import json

# Create your views here.
def index(request):
	movies = list(Movie.objects.values())
	return JsonResponse({'data':movies}, safe=False)

def create(request):
	body_json = json.loads(request.body)
	print(body_json)
	valid = validate_request(body_json)
	if not valid:
		return HttpResponse('Incomplete request')
	else:
		valid = sanitize_data(request)
		Movie.objects.create(name=body_json['name'], director=body_json['director'], imdb_score=body_json['imdb_score'], popularity=body_json['popularity'], genres=body_json['genres'])
		return HttpResponse('Check database')

def validate_request(body_json):
	valid = True
	if 'name' not in body_json or 'imdb_score' not in body_json or 'director' not in body_json or 'popularity' not in body_json or 'genres' not in body_json:
		valid = False
	return valid

def sanitize_data(request):
	valid = True
	#Formatting genres to store correctly
	return valid

def edit(request, id):
	try:
		m = Movie.objects.get(id=id)
		return JsonResponse({'data': model_to_dict(m)}, safe=False)
	except Movie.DoesNotExist:
		return HttpResponse('Dude no such movie man!')

def update(request, id):
	try:
		body_json = json.loads(request.body)
		valid = validate_request(body_json)
		if not valid:
			return HttpResponse('Incomplete request')
		else:
			valid = sanitize_data(request)
			m = Movie.objects.filter(id=id).update(name=body_json['name'], director=body_json['director'], imdb_score=body_json['imdb_score'], popularity=body_json['popularity'], genres=body_json['genres'])		
			return JsonResponse({'data': body_json}, safe=False)
	except Movie.DoesNotExist:
		return HttpResponse('Dude no such movie man!')

def delete(request, id):
	try:
		Movie.objects.filter(id=id).delete()
		return JsonResponse('Successful deletion', safe=False)
	except Movie.DoesNotExist:
		return HttpResponse('Dude no such movie man!')

def search(request):
	if 'q' not in request.GET:
		return HttpResponse('Dude nothing to search for')
	else:
		search = request.GET['q']
		results = list(Movie.objects.filter(Q(name__icontains=search) | Q(director__icontains=search) | Q(genres__icontains=search)).values())
		return JsonResponse({'data': results}, safe=False)	
					