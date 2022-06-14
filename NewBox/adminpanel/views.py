from django.http import HttpResponseRedirect
from django.shortcuts import render


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    return render(request, 'login.html')
