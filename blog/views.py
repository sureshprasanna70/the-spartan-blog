from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.
def index(request):
	html = "<html><body>It is now</body></html>"
	return HttpResponse(html)

