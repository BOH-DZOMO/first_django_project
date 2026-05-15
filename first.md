## Environment variables

This are used to securely store sensitive data like secret keys, database credentials  
SOme common methods are:
os.environ : a python dict that aalows you to interact with the environment varaibles of the os it is running
django-environ: A library for environment vcaraibles for Django that supports data type casting

## Middlewares
It acts as a series of lightweight, low-level plugin layers that sit between the user's browser and your Django views.
it acts both on reuest and response

the self.get_response is used to send a request to the next middle ware when called in __call__ and python pauses the middle ware and it only resumes on the next line when the view has finished and the request response is going back to the user. The return response in __call__ send it to the middle ware closer to the user when resonse is leaving


## Models
model fields
filter lookup
Model manager(objects)
https://djangocentral.com/django-orm-cheatsheet/
models.F
models.Q
models.OnetoOne =Field()
models.ForeignKey()
models.ManytoManyField()
Meta class are extra attributes of our model 
(db_table,ordering,get_latest by,verbose_name,abstract)




## Views
A view is a callable which takes a request and returns a response.

request ---> url router --> View ---><---[QuerySet] ---><--- Model/Databse

View --->Template --->HTML

urlconf
reverse
url template tag 
| operator(filter)



generic views
