from django.shortcuts import render, render_to_response, HttpResponseRedirect, Http404
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from photos.forms import PictureForm
from django.core.context_processors import csrf
# Create your views here.

def add_photos_view(request):
	if request.POST:
		form = PictureForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
	    form = PictureForm()

	args = {}
	args.update(csrf(request))

	args['form'] = form

	return render(request,'addPhoto.html')