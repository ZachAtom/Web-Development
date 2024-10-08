from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

posts = [
    {
        'name': 'Jackson',
        'roll': '12',
        'address': 'Thongju',
        'department': 'Computer Science'
    },
    {
        'name': 'Tom',
        'roll': '13',
        'address': 'Singjamei',
        'department': 'Physics'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'django_app/home.html',context)
def about(request):
    return render(request, 'django_app/about.html', {'title': 'Zach'})

