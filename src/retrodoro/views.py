from django.http import HttpResponse
from django.shortcuts import render
from .utils.db_util import user_exists, add_user


def login(request):
    return render(request, 'retrodoro/login.html')

def loginuser(request):
    if request.POST:
        request_data = request.POST.dict()
        username = request_data.get("username")
        password = request_data.get("password")
        if not user_exists:
            add_user(username, password)
            return render(request, 'retrodoro/login.html')

    return render(request, 'retrodoro/login.html')