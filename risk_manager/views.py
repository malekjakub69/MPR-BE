from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from django.http import *
from django.contrib.auth import authenticate, login, logout
# from .models import User


def random(request, pk):
    if request.method == 'GET':
        data = {'req': 'GET', 'key': pk}
        return JsonResponse(data)
    elif request.method == 'POST':
        data = {'req': 'GET', 'key': pk}
        return JsonResponse(data)
    else:
        return HttpResponseNotFound


def get_user(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseForbidden
    if request.method == 'GET':
        # user = Entry.objects.get(pk=pk)
        user = {'none'}
        return JsonResponse(user)
    else:
        return HttpResponseBadRequest


def login_user(request):
    if request.method != 'POST':
        return HttpResponseBadRequest
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return user
    else:
        return HttpResponseForbidden


def logout_user(request):
    logout(request)


def get_users(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden
    if request.method == 'GET':
        # users = User.objects.all()
        users = {'none'}
        return JsonResponse(users)
    else:
        return HttpResponseBadRequest


def get_projects(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden
    if request.method == 'GET':
        # projects = Projects.objects.all()
        user = {'none'}
        return JsonResponse(user)
    else:
        return HttpResponseBadRequest


def get_project(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseForbidden
    if request.method == 'GET':
        # user = Projects.objects.get(pk=pk)
        user = {'none'}
        return JsonResponse(user)
    else:
        return HttpResponseBadRequest


def get_risks(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseForbidden
    if request.method == 'GET':
        # risks = Risks.objects.filter(project=pk)
        risks = {'none'}
        return JsonResponse(risks)
    else:
        return HttpResponseBadRequest


def get_risk(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseForbidden
    if request.method == 'GET':
        # user = Ristks.objects.get(pk=pk)
        user = {'none'}
        return JsonResponse(user)
    else:
        return HttpResponseBadRequest
