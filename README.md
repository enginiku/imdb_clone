# imdb_clone
Simple REST APIs for movies, allows users to add, view, update, delete and search movies - only with appropriate access. Each user is given an 'API KEY' to be used to perform the above actions. The API KEY needs to sent as a custom header named 'api-key' to access any of the APIs. All the APIs have been tested using POSTMAN. Details about the APIs are given below.


### API Details
The Python-Django app is deployed on Heroku with MySQL as the database. All requests/responses are in json format. The base URL is -
```
https://imdb-api-clone.herokuapp.com/
```

#### 1. List all movies
```
GET movies/list
```
This API returns the complete list of movies without any filters and is open to all users.

#### 2. Add a movie
```
POST movies/create
```
This API allows only admins to create a new movie record. An example of the request body is - 
 ```
 {
	"name": "Black Friday",
	"director": "Anurag Kashyap",
	"popularity": 40.0,
	"imdb_score": 8.5,
	"genres": "Drama, Crime, Action"
}
```

#### 3. Update a movie
```
PUT movies/<id>/update
```
This API updates details of the movie having given id. An example of the request body is -
```
{
	"name": "Black Friday",
	"director": "Anurag Kashyap",
	"popularity": 65.0,
	"imdb_score": 8.5,
	"genres": "Drama, Crime, Action, Adaptation"
}
```

#### 4. View a movie
```
GET movies/<id>/edit
```
This API returns a single movie record having given id.

#### 5. Delete a movie
```
DELETE movies/<id>/delete
```
This API allows admins to delete a movie record having given id.

#### 6. Search movies
```
GET movies/search?q=<search_string>
```
This API returns a list of movies based on the given search term. The parameter 'q' is required.


### Future scalability
To cater to 15M users accessing 5M movies on the platform, the current architecture will create a bottleneck in terms of database performance as well as memory.

It would be ideal to have a NoSQL database like ElasticSearch and use it's indexing capabilities to speed up the look up time.

The other change would be to increase the number of dynos if using Heroku or altogether migrate to AWS to have a tighter control over the infrastructure like choosing high performance EC2 instances.

Besides we can also add pagination to the APIs
