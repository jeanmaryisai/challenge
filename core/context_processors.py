from .models import *

def cart(request):
    concurents= Concurent.objects.all()
    dedicaces= Dedicace.objects.filter(show=True).order_by('-date')[:5]
    notification=Notification.objects.all().order_by('-date')[:5]
    context={'concurents':concurents
    ,
    'dedicaces':dedicaces,
    'notifications':notification,

    }
    return context