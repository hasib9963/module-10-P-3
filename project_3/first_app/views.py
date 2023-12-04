from django.shortcuts import render
import datetime
# Create your views here.


def home(request):
    d = {'author' : 'Rahim', 'age' : 5, 'lst': ['python','is','best'], 'birthday' : datetime.datetime.now(),  'val' : '','courses' : [
        {
            'id' : 1,
            'name' : 'Python',
            'fee' : 5000
            
        },
        {
            'id' : 2,
            'name' : 'Django',
            'fee' : 4780  
        },
        {
            'id' : 3,
            'name' : 'C++', 
            'fee' : 4320 
        }
    ]}
    return render(request, 'home.html', d)