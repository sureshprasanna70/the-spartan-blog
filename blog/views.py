from django.shortcuts import render_to_response
from django.http import HttpResponse
from blog.models import Blog_Post
# Create your views here.
def index(request):
	#getting count
	publisher=Blog_Post.objects.all().count()
	#getting all
	for e in Blog_Post.objects.all():
    		print(e)
	
	return HttpResponse(publisher)

