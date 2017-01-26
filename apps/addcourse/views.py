from django.shortcuts import render, HttpResponse, redirect
from .models import Course

# Create your views here.

def index(request):
    courses = Course.objects.all()


    # context = { 'courses': courses}

    context = { 'courses': courses}

    if "name" not in request.session:
        request.session['name']=''
        request.session['description']=''

    # print courses.query
    return render(request, 'addcourse/index.html', context)

def addcourse(request):
    request.session['name']= request.POST['name']
    request.session['description']= request.POST['description']
    Course.objects.create(name=request.session['name'],description=request.session['description'])



    # print request.session['name']
    # print request.session['description']
    return redirect('/')

def deletecourse(request, id):
    print id
    request.session['idcarry']=id
    todelete= Course.objects.get(id=id)
    context={
    "todelete":todelete
    }

    return render(request, 'addcourse/index2.html',context, id)
def cancel(request):
    return redirect('/')
def deleteconfirm(request, id):
    # print request.session['idcarry']
    print id
    Course.objects.filter(id=id).delete()
    return redirect('/')
