from django.shortcuts import render_to_response
from django.http import HttpResponse
from blog.models import Blog_Post
# Create your views here.
def index(request):
	#getting count
	publisher=Blog_Post.objects.all().count()
	All_post=[]
	for i in range(0,publisher):
			All_post.append([Blog_Post.objects.all()[i].title,Blog_Post.objects.all()[i].contents])
			
	return render_to_response('index.html', {'title':"Spartanz Blog",'content':All_post,'totalCount':i})
