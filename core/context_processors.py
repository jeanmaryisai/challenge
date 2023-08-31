from .models import *
from .utils import *

def cart(request):
    concurents= Concurent.objects.all()
    dedicaces= Dedicace.objects.filter(show=True,event=True).order_by('-date')[:5]
    notification=Notification.objects.all().order_by('-date')[:5]
    context={'concurents':concurents
    ,
    'dedicaces':dedicaces,
    'notifications':notification,
    'event':CustomEvent.objects.get(isActive=True)

    }
    return context