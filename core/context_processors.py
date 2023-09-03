from .models import *
from .utils import *

def cart(request):
    concurents= Concurent.objects.all()
    dedicaces= Dedicace.objects.filter(show=True,event=True).order_by('-date')[:5]
    notification=Notification.objects.all().order_by('-date')[:5]
    event=[]
    try:
        CustomEvent.objects.get(isActive=True)
    except:
        pass
    context={'concurents':concurents
    ,
    'dedicaces':dedicaces,
    'notifications':notification,
    'event':event

    }
    return context