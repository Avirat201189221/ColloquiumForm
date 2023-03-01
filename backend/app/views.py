from django.shortcuts import render

# Create your views here.
def register(request):

    return render(request, "register.html") 

def sucess(request):

    return render(request,"success.html")

def mss(request):

    return render(request,"mandss.html")

def code(request):

    return render(request,"codeoclock.html")

def cc(request):

    return render(request,"theclowncanard.html")