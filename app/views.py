from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def starbugs(request):
    return HttpResponse('Worst chai is available in starbugs')
