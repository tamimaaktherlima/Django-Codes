from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def home(request):
    d = {'author' : 'Rahim', 'age' : 15, 'list':[1,2,3],'date':datetime.datetime.now(),'list1':['python','is','best'],'courses':[
        {
            'id' : 1,
            'name' : 'python',
            'fees' : 1000
        } ,
        {
            'id' : 2,
            'name' : 'Django',
            'fees' : 5000
        } ,
        {
            'id' : 3,
            'name' : 'data structure',
            'fees' : 2000
        } ,
        {
            'id' : 4,
            'name' : 'algorithm',
            'fees' : 4000
        } 
        
    ]}
    return render(request,'home.html',d)


