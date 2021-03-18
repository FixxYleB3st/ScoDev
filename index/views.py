from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

import project584.global_var as gv

# Create your views here.
def index(request):
	context = {'user': request.user}
	return render(request, 'index/index.html', context)