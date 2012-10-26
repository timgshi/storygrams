from django.http import HttpResponse, HttpResponseRedirect
from storygram.Frameworks import ParsePy
# from Frameworks.python-instagram import instagram

def subscription(request):
	print request
	if request.method == 'GET':
		challenge = request.GET['hub.challenge']
		return HttpResponse(challenge)

