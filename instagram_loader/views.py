from django.http import HttpResponse, HttpResponseRedirect
from Frameworks import ParsePy
import json
# from Frameworks.python-instagram import instagram

def index(request):
	print "index"
	return HttpResponse('hi')

def subscription(request):
	print request
	if request.method == 'GET':
		challenge = request.GET['hub.challenge']
		return HttpResponse(challenge)
	elif request.method == 'POST':

		print request

