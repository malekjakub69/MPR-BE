from django.http import *
from django.contrib.auth import authenticate, login, logout
from .models import User, Project, Risk
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
# from .helper import authenticate
from django.contrib.auth.hashers import make_password
from datetime import datetime

def create_fake_user(request):
    email = "test5"
    user = User.objects.all().filter(email=email).first()
    if user is None:
        password = make_password(email)
        user = User.objects.create(password=password, name="test", surname="test", email=email, role="USER")
        data = serializers.serialize('json', [user, ])
        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponseBadRequest()


def check_user_logged(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    else:
        return HttpResponse()


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


@csrf_exempt
def create_project(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == 'POST':
        owner_id = request.POST["owner_id"]
        name = request.POST["name"]
        description = request.POST["description"]
        status = request.POST["status"]
        date_begin = request.POST["date_begin"]
        date_end = request.POST["date_end"]
        user = User.objects.get(pk=owner_id)
        begin = datetime.strptime(date_begin, "%Y-%m-%d").date()
        end = datetime.strptime(date_end, "%Y-%m-%d").date()
        if user is not None:
            project = Project.objects.create(
                owner_id=user,
                name=name,
                description=description,
                status=status,
                date_begin=begin,
                date_end=end
            )
            project = serializers.serialize('json', [project, ])
            return HttpResponse(project, content_type='application/json')
        else:
            return HttpResponseNotFound()
    else:
        return HttpResponseBadRequest()


def get_user_risks(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == 'GET':
        risk = Risk.objects.all().filter(owner=pk)
        if risk is not None:
            risk = serializers.serialize('json', risk)
            return HttpResponse(risk, content_type='application/json')
        else:
            return HttpResponseNotFound()
    else:
        return HttpResponseBadRequest()


def get_project_risks(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == 'GET':
        risk = Risk.objects.all().filter(project=pk)
        if risk is not None:
            risk = serializers.serialize('json', risk)
            return HttpResponse(risk, content_type='application/json')
        else:
            return HttpResponseNotFound()
    else:
        return HttpResponseBadRequest()


def get_risk(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == 'GET':
        risk = Risk.objects.get(pk=pk)
        if risk is not None:
            risk = serializers.serialize('json', risk)
            return HttpResponse(risk, content_type='application/json')
        else:
            return HttpResponseNotFound()
    else:
        return HttpResponseBadRequest()


def create_risk(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == 'POST':
        owner = request.POST[""]
        category = request.POST["owner"]
        project = request.POST["category"]
        title = request.POST["project"]
        description = request.POST["title"]
        danger = request.POST["description"]
        trigger = request.POST["danger"]
        reactions = request.POST["trigger"]
        probability = request.POST["reactions"]
        impact = request.POST["probability"]
        status = request.POST["impact"]
        date_identified = request.POST["status"]
        date_updated = request.POST["date_identified"]
        date_reaction = request.POST["date_updated"]
        user = User.objects.get(pk=owner)
        if user is not None:
            project = Project.objects.get(pk=project)
            if project is not None:
                risk = Risk.objects.create(
                    owner=owner,
                    category=category,
                    project=project,
                    title=title,
                    description=description,
                    danger=danger,
                    trigger=trigger,
                    reactions=reactions,
                    probability=probability,
                    impact=impact,
                    status=status,
                    date_identified=date_identified,
                    date_updated=date_updated,
                    date_reaction=date_reaction
                )
                risk = serializers.serialize('json', risk)
                return HttpResponse(risk, content_type='application/json')
            else:
                return HttpResponseNotFound()
        else:
            return HttpResponseNotFound()
    else:
        return HttpResponseBadRequest()


def update_risk(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == 'POST':
        owner = request.POST[""]
        category = request.POST["owner"]
        project = request.POST["category"]
        title = request.POST["project"]
        description = request.POST["title"]
        danger = request.POST["description"]
        trigger = request.POST["danger"]
        reactions = request.POST["trigger"]
        probability = request.POST["reactions"]
        impact = request.POST["probability"]
        status = request.POST["impact"]
        date_identified = request.POST["status"]
        date_updated = request.POST["date_identified"]
        date_reaction = request.POST["date_updated"]
        user = User.objects.get(pk=owner)
        if user is not None:
            project = Project.objects.get(pk=project)
            if project is not None:
                risk = Risk.objects.update(
                    owner=owner,
                    category=category,
                    project=project,
                    title=title,
                    description=description,
                    danger=danger,
                    trigger=trigger,
                    reactions=reactions,
                    probability=probability,
                    impact=impact,
                    status=status,
                    date_identified=date_identified,
                    date_updated=date_updated,
                    date_reaction=date_reaction
                )
                risk = serializers.serialize('json', risk)
                return HttpResponse(risk, content_type='application/json')
            else:
                return HttpResponseNotFound()
        else:
            return HttpResponseNotFound()
    else:
        return HttpResponseBadRequest()


def update_project(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == 'POST':
        owner_id = request.POST["owner_id"]
        name = request.POST["name"]
        description = request.POST["description"]
        status = request.POST["status"]
        date_begin = request.POST["date_begin"]
        date_end = request.POST["date_end"]
        user = User.objects.get(pk=owner_id)
        if user is not None:
            project = Project.objects.update(
                owner_id=owner_id,
                name=name,
                description=description,
                status=status,
                date_begin=date_begin,
                date_end=date_end
            )
            project = serializers.serialize('json', project)
            return HttpResponse(project, content_type='application/json')
        else:
            return HttpResponseNotFound()
    else:
        return HttpResponseBadRequest()

