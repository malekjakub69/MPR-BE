from django.http import *
from django.contrib.auth import authenticate, login, logout
from .models import User, Project
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
# from .helper import authenticate
from django.contrib.auth.hashers import make_password


def get_user(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == 'GET':
        user = User.objects.get(pk=pk)
        if user is not None:
            data = serializers.serialize('json', [user, ])
            return HttpResponse(data, content_type='application/json')
        else:
            return HttpResponseNotFound()
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def login_user(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    # User.objects.all().filter(email="test").first().delete()
    username = request.POST["email"]
    pwd = request.POST["password"]
    user = authenticate(request=request, email=username, password=pwd)
    if user is not None:
        login(request, user)
        data = serializers.serialize('json', [user, ])
        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponseForbidden()


@csrf_exempt
def logout_user(request):
    logout(request)
    return HttpResponse()


def get_users(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == 'GET':
        users = serializers.serialize('json', User.objects.all())
        return HttpResponse(users, content_type='application/json')
    else:
        return HttpResponseBadRequest()


def get_projects(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == 'GET':
        projects = serializers.serialize('json', Project.objects.all())
        return HttpResponse(projects, content_type='application/json')
    else:
        return HttpResponseBadRequest()


def get_project(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == 'GET':
        project = Project.objects.get(pk=pk)
        if project is not None:
            project = serializers.serialize('json', project)
            return HttpResponse(project, content_type='application/json')
        else:
            return HttpResponseNotFound()
    else:
        return HttpResponseBadRequest()


def create_project(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == 'POST':
        # User.objects.create(password=make_password("test"), name="test", surname="test", email="test", role="USER")
        # project = Projects.objects.get(pk=pk)
        project = {'none'}
        return JsonResponse(project)
    else:
        return HttpResponseBadRequest()


def get_risks(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == 'GET':
        # risks = Risks.objects.filter(project=pk)
        risks = {'none'}
        return JsonResponse(risks)
    else:
        return HttpResponseBadRequest()


def get_risk(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == 'GET':
        # user = Ristks.objects.get(pk=pk)
        user = {'none'}
        return JsonResponse(user)
    else:
        return HttpResponseBadRequest()


def create_risk(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == 'POST':
        # risk = Projects.objects.get(pk=pk)
        risk = {'none'}
        return JsonResponse(risk)
    else:
        return HttpResponseBadRequest()

def update_risk(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == 'POST':
        # risk = Projects.objects.get(pk=pk)
        risk = {'none'}
        return JsonResponse(risk)
    else:
        return HttpResponseBadRequest()

def update_project(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == 'POST':
        # project = Projects.objects.get(pk=pk)
        project = {'none'}
        return JsonResponse(project)
    else:
        return HttpResponseBadRequest()

