from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    if request.method == "GET":
        form = UserCreationForm()

    if request.method == "POST":
        print(request.POST)

    return render(request, "user/register.html", {"form": form})
