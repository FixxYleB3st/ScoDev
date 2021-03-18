from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import project584.global_var as gv

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
	template = loader.get_template("sellers/sellers.html")
	context = {
	}
	return HttpResponse(template.render(context, request=request))