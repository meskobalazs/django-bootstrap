from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'mozillaq/index.html')

def list(request):
	return HttpResponse('{"this": 1, "is": "just", "sample": ["text", "content", "here"]}', status=200)
