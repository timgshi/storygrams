from django.http import HttpResponse, HttpResponseRedirect
from Frameworks import ParsePy
import json
from instagram import InstagramAPI

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
			try:
				photo = api.media(obj['object_id'])
				parse_photo = ParsePy.ParseObject("instagram_photo")
				parse_photo.url = photo.images['standard_resolution'].url
				parse_photo.url_thumb = photo.images['thumbnail'].url
				parse_photo.timestamp = photo.created_time
				likes = []
				for user in photo.likes:
					likes.append(parse_user_from_instagram(user))
				parse_photo.likes = likes;
				comments = []
				for comment in photo.comments:
					comments.appent(parse_comment_from_instagram(comment))
				parse_photo.comments(comments)
				parse_photo.location = parse_location_from_instagram(photo.location)
				parse_photo.save()
			except AttributeError:
				pass
		print request

def parse_user_from_instagram(user):
	userResponse = ParsePy.ParseQuery("instagram_user").equal("instagram_id", user.id).fetch()
	if userResponse[0] != None:
		return userResponse[0]
	else:
		newUser = ParsePy.ParseObject("instagram_user")
		newUser.username = user.username
		newUser.instagram_id = user.id
		newUser.full_name = user.full_name
		newUser.profile_picture = user.profile_picture
		newUser.save()
		return newUser

def parse_comment_from_instagram(comment):
	commentResponse = ParsePy.ParseQuery("instagram_comment").equal("instagram_id", comment.id).fetch()
	if commentResponse[0] != None:
		return commentResponse[0]
	else:
		newComment = ParsePy.ParseObject("instagram_comment")
		newComment.user = parse_user_from_instagram(comment.user)
		newComment.instagram_id = comment.id
		newComment.timestamp = comment.created_at
		newComment.text = comment.text
		newComment.save()
		return newComment

def parse_location_from_instagram(location):
	locationResponse = ParsePy.ParseQuery("instagram_location").equal("instagram_id", location.id).fetch()
	if locationResponse[0] != None:
		return locationResponse[0]
	else:
		newLocation = ParsePy.ParseObject("instagram_location")
		newLocation.instagram_id = location.id
		newLocation.name = location.name
		newLocation.point = ParsePy.ParseGeoPoint(location.point.latitude, locatoin.point.longitude)
		return newLocation

