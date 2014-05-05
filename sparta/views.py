from django.shortcuts import render_to_response
from django.utils import simplejson
from blog.models import Blog_Post
import datetime
def index(request):
	Title=Blog_Post.objects.all()[0].title
	Contents=Blog_Post.objects.all()[0].contents
	publisher=Blog_Post.objects.all().count()
	print (publisher)
	All_title=[]
	All_post=[]
	for i in range(0,publisher):
			All_title.append([Blog_Post.objects.all()[i].title,Blog_Post.objects.all()[i].contents])
			All_post.append(Blog_Post.objects.all()[i].contents)
	#return HttpResponse(contents)
	
	return render_to_response('index.html', {'title':All_title,'content':All_post,'totalCount':i})



