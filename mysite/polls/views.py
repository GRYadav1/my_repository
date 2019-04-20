from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from sklearn_nn import test_Model
print("CHeckCOmping")
from sklearn_nn import train_model
print("End Compile")

pathString ="E:/Chrome-Downloads/VA/"
clf = None
def index(request):
    template = loader.get_template('polls/index.html')
    print("Hi index")
    global clf
    clf = train_model();
    return HttpResponse(template.render({}, request))

def imageSubmit(request):
    print("Hi imageSubmit")
    if 'q' in request.GET:
        pathString1=pathString+request.GET['p']
        pathString2= pathString+request.GET['q']
        print(pathString1,pathString2);
        global clf
        message=test_Model('data/test/050/01_050.PNG','data/test/050_forg/01_0125050.PNG',clf)
        print("Final Sore :",message)

        #pathString+=request.GET['q']
    else:
        message = 'You know nothing Jon Snow!'
        print(message)
    return HttpResponse(message)
