# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import a_description

# Create your views here.
def index(request):
	template = loader.get_template("about/about.html")
	context = {
		'user': request.user
	}
	return HttpResponse(template.render(context, request=request))