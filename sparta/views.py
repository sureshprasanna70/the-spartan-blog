from django.shortcuts import render_to_response
from django.http import HttpResponse
from blog.models import Blog_Post
import datetime
def index(request):
	Title=Blog_Post.objects.all()[0].title
	Contents=Blog_Post.objects.all()[0].contents
	#print (publisher)
	contents=["name"]
	#for i in range(0,publisher):
	#		contents[i]=Blog_Post.objects.get(id=i+1)
	#return HttpResponse(contents)
	return render_to_response('index.html', {'title':Title,'content':Contents})



