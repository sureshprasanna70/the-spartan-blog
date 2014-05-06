from django.shortcuts import render_to_response
from django.utils import simplejson
from blog.models import Blog_Post
import datetime
def index(request):
	return render_to_response('index.html',{'title':'HOME'})

	



