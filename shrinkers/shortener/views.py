from shortener.models import Users
from django.shortcuts import redirect, render

# Create your views here.


def index(request):
    # user = Users.objects.get(username="admin") # get은 반드시 1개만 가져옴
    user = Users.objects.filter(username="admin").first() # 어떤값이 들어올지 몰라 filter로 
    email = user.email if user else "Anonymous User!"
    print(email)
    print(request.user.is_authenticated)
    if request.user.is_authenticated is False:
        email = "Anonymous User!"
    print(email)
    return render(request, "base.html", {"welcome_msg": f"Hello {email}FastCampus!","hello" : "world"})


def redirect_test(request):
    print("Go Redirect")
    return redirect("index")