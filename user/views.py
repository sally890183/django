from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    message = ""
    form = UserCreationForm()

    if request.method == "POST":
        print(request.POST)

        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # 密碼長度8
        if len(password1) != 8 or len(password2) != 8:
            message = "密碼長度不正確"
        elif password2 != password1:
            message = "兩次密碼不一樣"

    return render(request, "user/register.html", {"form": form, "message": message})
