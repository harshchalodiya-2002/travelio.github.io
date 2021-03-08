from django.shortcuts import render
from home.models import contact,places
# Create your views here.
def home(request):
    obj = places.objects.all()
    return render(request,'Home.html',{'objects':obj})

def second(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        c = contact(fname=name,email=email,phone=phone)
        c.save()


    return render(request,'contact.html')