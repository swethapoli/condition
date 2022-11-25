from django.shortcuts import render

# Create your views here.
def jinja_tag(request):
    d={'name':'swetha','age':20}
    return render(request,'jinja_tag.html',d)
def condition(request):
    d={'a':300,'b':200,'c':400}
    return render(request,'condition.html',d)
