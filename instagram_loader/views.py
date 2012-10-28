from django.http import HttpResponse, HttpResponseRedirect
from Frameworks import ParsePy
import json
import instagram

def index(request):
	print "index"
	return HttpResponse('hi')

def subscription(request):
	print request
	if request.method == 'GET':
		challenge = request.GET['hub.challenge']
		return HttpResponse(challenge)
	elif request.method == 'POST':
		subscription_objects = json.loads(request.body)
		api = InstagramAPI(client_id=INSTAGRAM_CLIENT_ID, client_secret=INSTAGRAM_CLIENT_SECRET)
		for obj in subscription_objects:
			photo = api.media(obj['object_id'])
			print photo
		print request

