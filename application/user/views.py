from django.http import HttpResponseRedirect
from django.contrib import auth


def login_process(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/")
    else:
        # Show an error page
        return HttpResponseRedirect("/")


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
