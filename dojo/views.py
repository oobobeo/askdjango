from django.shortcuts import render
import os

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.conf import settings

def mysum(request, nubmers):
	return HttpResponse(nubmers)

def list1(request):
	name = 'bobe'
	return HttpResponse(f'''
		<h> hello! </h>
		<p> {name} </p>
		<p> whatever </p>

		''')

def list2(request):
	name = 'bobe'
	return render(request, 'dojo/post_list.html', {'name':name})


def list3(request):
	list_ = ['a', 'b', 'c', 'd', 'e']
	return render(request, 'dojo/list3.html', {'list':list_})