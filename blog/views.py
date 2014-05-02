from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.
def index(request):
	html = "<html><body>djfks</body></html>"
	return HttpResponse(html)

