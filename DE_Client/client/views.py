from django.shortcuts import *
from django.http import *
from django.template import RequestContext
from client.forms import *
# add authencation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.db import connections
import json
import math


def login(request):
    logout(request)
    return render(request, 'client/login.html', {'form': userLoginForm(), 'error': ''})

# Here handle the login in form validation, wish to change it into model later

def validation(request):
    logout(request)
    username = ''
    password = ''

    if (request.method == 'POST'):
        form = userLoginForm(request.POST)

        if (form.is_valid()):
            username = request.POST['userID_email']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if(user is not None):
                if(user.is_active):
                    auth_login(request, user)
                    return HttpResponseRedirect('app')

        # else:
        #     error = 'ID/Email or password is not correct'
        #     return render_to_response('client/login.html', {'form': userLoginForm(), 'error': 'this is just a test'}, context_instance=RequestContext(request))
        return render_to_response('client/login.html', {'form': userLoginForm(), 'error': 'this is just a test'}, context_instance=RequestContext(request))

@login_required()
def app(request):
    selected = ["selected", "default", "default", "default"]
    return render(request, 'client/main.html', {
        'user': selected[0],
        'product': selected[1],
        'view': selected[2],
        'notice': selected[3],
    })

@login_required()
def product(request):
    selected = ["default", "selected", "default", "default"]

    return render(request, 'client/product.html', {
        'user': selected[0],
        'product': selected[1],
        'view': selected[2],
        'notice': selected[3],
    })

@login_required()
def m_view(request):

    # TODO: time range should get from database

    selected = ["default", "default", "selected", "default", "2015/07/20 - 2015/08/29"]

    return render(request, 'client/view.html', {
        'user': selected[0],
        'product': selected[1],
        'view': selected[2],
        'notice': selected[3],
        'timeRange': selected[4],
    })

@login_required()
def notification(request):
    selected = ["default", "default", "default", "selected"]
    db_conn = connections['default']
    cursor = db_conn.cursor()
    # get current login user name for further query in term of message
    current_user = request.user.username
    cursor.execute("select body from message where designer like %s ORDER BY updated_at DESC ", ["Gary Zheng"])
    data = cursor.fetchall()
    db_conn.commit()
    cursor.close()
    db_conn.close()
    if len(data) <= 5:
        return render(request, 'client/notification.html', {
            'user': selected[0],
            'product': selected[1],
            'view': selected[2],
            'notice': selected[3],
            'datalist': data
        })
    else:

        return render(request, 'client/notification.html', {
            'user': selected[0],
            'product': selected[1],
            'view': selected[2],
            'notice': selected[3],
            'datalist': data[:5]
        })

@login_required()
def postNotification(request):

    if(request.is_ajax() and request.POST):

        # TODO: database connection
        db_conn = connections['default']
        cursor = db_conn.cursor()
        cursor.execute("select body from message where designer like %s ORDER BY updated_at DESC ", ["Gary Zheng"])
        original = cursor.fetchall()
        count = math.ceil(len(original) / 5)
        db_conn.commit()
        cursor.close()
        db_conn.close()
        if(request.POST["message"] == "previous"):
            index = request.POST["index"]
            start = int(index)*5
            end = (int(index)+1)*5
            data = original[start:end]
        if(request.POST["message"] == "next"):
            index = request.POST["index"]
            if(int(index) >= count):
                data = ['error', count]
            else:
                start = int(index)*5
                end = (int(index)+1)*5
                data = original[start:end]
        return HttpResponse(json.dumps(data), content_type='application/json')

    else:
        raise Http404














