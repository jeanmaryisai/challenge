
from decimal import Decimal
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from datetime import datetime
from django.contrib.admin.views.decorators import staff_member_required


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        user_Fake,created=fake_user.objects.get_or_create(user=request.user)

    manches=Manche.objects.all().order_by('numero')

    a=Question.objects.exclude(receveur__isnull=True).count()
    b=Question.objects.filter(repondu=True).count()
    c=Question.objects.filter(repondu=False).exclude(receveur__isnull=True).exclude(repliques__isnull=True).count()
    d=a-b-c
    p=Programme.objects.filter(passe=False).order_by('rank')
    pp_first=p.first()
    pp_last=p.last()
    p_percent=int((pp_first.rank/pp_last.rank) * 100) 
    xxx=0
    xx=0
    xxy=0
    try:
        xxx=int((b/a) * 100)
        xx=int((c/a) * 100)
        xxy=int((d/a) * 100)
    except:
        xxx=0
    
    context={
        'programmes':p,
        'manches':manches,
        'manche_active':Manche.objects.filter(isopen=True).order_by('numero').first,
        'previous_manche':Manche.objects.filter(isopen=False).order_by('numero').last,
        'notification':Notification.objects.all().order_by('-date')[:10],
        'questions_ans':xxx,
        'questions_replique':xx,
        'questions_missed':xxy,
        'p_percent':p_percent,
        'concurents':Concurent.objects.all(),
        'user':fake_user,
    }
    return render(request,'index.html',context)

def concurent(request,slug):
    manche=Manche.objects.filter(isopen=True).order_by('numero').first()
    if(slug=='all'):
        context={
            'manche':manche,
        }
        return render(request,'concurents.html',context)
    else:
        try:
            concurent= Concurent.objects.get(nom=slug)
            numero=manche.numero
            x=concurent.position_manche[numero-1]
            y=concurent.position_manche[numero-2]
            if numero==1:
                y=''
            if x==1:
                x='Premiere position pour cette manche'
            else:
                x=f'{x}eme position pour cette manche'

            if y==1:
                y='Premiere position pour la derniere manche'
            else:
                y=f'{y}eme position pour la derniere manche'

            logs=Logs.objects.filter(concurent=concurent).order_by('date')
            ip=get_client_ip(request)
        
            context={'concurent':concurent,
                'x':x,
                'y':y,
                'logs':logs,
                'manche':manche.concurent.get(concurent=concurent),
                'notifs':Notification.objects.filter(responsible=concurent).order_by('-date')

            }
            try:
                con=fake_user.objects.get(user=request.user)
                if con.concurent_fav is not None:
                    if con.concurent_fav == concurent:
                        context['fav']= 1
                    else:
                        context['fav']=2
            except:
                pass
            return render(request,'concurent.html',context)
        except:
            return redirect('home')
        
@staff_member_required
def question(request,slug):
    concurent=Concurent.objects.get(nom=slug)
    context={
        'question':Question.objects.all().first(),
        'concurent':concurent,
        'manche':Manche.objects.filter(isopen=True).order_by('numero').first(),
        'concurents': Concurent.objects.exclude(nom=concurent.nom),
    }
    return render(request,'question.html',context)

def questions(request):
    return render(request,'questions.html',{'qst':Question.objects.filter(used=True).order_by('number')})

def dedicaces(request):
    context={'dedicace':Dedicace.objects.filter(show=True)}
    try:
            # ip=get_client_ip(request)
            # concurent=fake_user.objects.get(ip=ip)
            concurent=fake_user.objects.get(user=request.user)
            context['user']=concurent
    except:
            pass
    return render(request,'dedicaces.html',context)

def remerciments(request):
    return render(request,'remerciments.html')

def notifications(request):
    return render(request,'notifications.html',{'notifs':Notification.objects.order_by('-date')})

def programme(request):
    p=Programme.objects.filter(passe=False).order_by('rank').first()
    try:
        next=Programme.objects.filter(passe=False).order_by('rank')[1]
    except:
        next=None
    context={
        'progs':Programme.objects.all(),
        'present':p,
        'next':next,
    }
    return render(request,'programme.html',context)

def dedicace(request):
    if request.method=='POST':
        destinataire=request.POST['destinataire']
        destinateur=request.POST['destinateur']
        msj=request.POST['msj']
        responsible=''
        try:
            id=request.POST['id']
            concurent=Concurent.objects.get(id=id)
            responsible=concurent
        except:
            pass
        yy=Dedicace.objects.create(emetteur=destinateur,recepteur=destinataire,message=msj,show=True)
        try:
            id_reponse=request.POST['replique']
            yy.replique_a=Dedicace.objects.get(id=id_reponse)
            yy.save()
        except:
            pass

        try:
            x=Notification.objects.create(message=f'{destinateur} a fait une dedicace a {destinataire}',responsible=responsible,level='i')
        except:
            x=Notification.objects.create(message=f'{destinateur} a fait une dedicace a {destinataire}',level='i')
        messages.success(request,'Votre dedicace a ete publie avec succes')
        return redirect('dedicaces')
    else:
        messages.error(request,'Nous avons du mal a traiter votre dedicace')
        return redirect('home')

@login_required
def vote(request,slug):
    if request.method=="GET":
        ip=get_client_ip(request)
        try:
            qs=fake_user.objects.get(user=request.user,concurent_fav__isnull=False)
            try:
                concurent=Concurent.objects.get(nom=slug)
                user=fake_user.objects.get(user=request.user,concurent_fav=concurent)
                user.concurent_fav=None
                user.save()
                messages.info(request,'Vous avez enlever votre vote.')
                return redirect('home')
            except:
                pass

            messages.error(request,'vous avez deja vote vous ne pouvez plus le faire')
            return redirect('home')
        except:
            pass
        if ip is None:
            messages.error(request,'nous avons du mal a traiter votre vote, si vous utiliser le mode incognito ou un vpn, enlever les et reesayer.')
            return redirect('home')
        concurent=''
        try:
            concurent=Concurent.objects.get(nom=slug)
        except:
            messages.error(request,"une erreur s'est produite")
            return redirect('home')
        user,created=fake_user.objects.get_or_create(user=request.user)
        user.concurent_fav=concurent
        user.save()
        messages.success(request,'vous avez votee avec succes!')
        return redirect ('home')
    else:
        return redirect('home')
    
@staff_member_required
def get_question(request,slug):
    if request.method=='POST':
        # try:
            num=int(slug)
            question= Question.objects.get(number=num)
            if question.used==True:
                messages.warning(request,'La question a deja ete utilsee')
                return JsonResponse(404,safe=False)
            jsonn=json.dumps(question.dump())
            return JsonResponse(jsonn,content_type='application/json',safe=False)
            
        # except:
        #     print('smth is wrong')
    else:
        return redirect('home')

@staff_member_required
def reponse(request):
    if request.method=='GET':
        return JsonResponse(400,safe=False)
    else:
        data=json.loads(request.body)
        reponse=data['reponse']
        question=Question.objects.get(number=data['question'])
        concurent=Concurent.objects.get(nom=data['concurent'])
        manche=Manche.objects.filter(isopen=True).order_by('numero').first()
        
        
        points=0
        mss='repondu a '
        lvl='s'

        if question.used:
            
            if reponse>=3:
                if concurent in question.repliques_rate.all():
                    messages.info(request,'Conflit de jugement veuillez gerer cette qst directement dans la section admin')
                    return JsonResponse(400,safe=False)
                if concurent in question.repliques.all():
                    messages.info(request,'Conflit de jugement veuillez gerer cette qst directement dans la section admin')
                    return JsonResponse(400,safe=False)
                if reponse==3:
                    points=Decimal(12.5) 
                    mss='repondu la replique a'
                elif reponse==4:
                    points=Decimal(-12.5) 
                    mss='rate la replique a'
                    lvl='d'
                messages.debug(request,'heoheo')
                
                
                
                question.repliques_rate.add(concurent)
                question.save()

                Notification.objects.create(responsible=concurent,message=f'A {mss} question #{question.number}',level=lvl)
                
                concurent.pointCum =points +concurent.pointCum
                concurent.save()

                for x in manche.concurent.all():
                    if x.concurent == concurent:    
                        x.pointsCum = points+x.pointsCum 
                        x.save()


                return JsonResponse(200,safe=False)


            messages.info(request,'La question a deja ete posee')
            return JsonResponse(400,safe=False)
  
        
        
        if reponse==1:
            reponse=True
            points=25
        else:
            reponse=False
            mss='rate '
            lvl='d'
       
        question.manche=manche
        question.receveur=concurent
        question.repondu=reponse
        question.used=True
        question.time_answer=datetime.now()
        question.save()
        
        concurent.pointCum +=points
        concurent.save()

        for x in manche.concurent.all():
            if x.concurent == concurent:    
                x.pointsCum += points
                x.save()
        

        Notification.objects.create(responsible=concurent,message=f'A {mss} la question #{question.number}',level=lvl)
                
        Logs.objects.create(concurent=concurent,question=question,pointsCum=concurent.pointCum,manche=manche.numero)

        return JsonResponse(200,safe=False)

@staff_member_required
def replique(request):
    if request.method=='GET':
        return JsonResponse(400,safe=False)
    else:
        data=json.loads(request.body)
        print(data)
        return JsonResponse(200,safe=False)

@login_required
def like(request,slug):
    if request.method=='POST':
        messages.warning(request,"une erreur s'est produite !")
        return redirect('home')
    else:
        dedicace=''
        try:
            dedicace=Dedicace.objects.get(id=slug)
        except:
            messages.info('Nous avons du mal a trouve votre dedicaces')
            return redirect('dedicaces')
        ip=get_client_ip(request)
        if ip is None:
            messages.error(request,'nous avons du mal a traiter votre vote, si vous utiliser le mode incognito ou un vpn, enlever les et reesayer.')
            return redirect('home')
        user,created=fake_user.objects.get_or_create(user=request.user)
        if dedicace in user.dedicaces.all():
            user.dedicaces.remove(dedicace)
            user.save()
            messages.warning(request,'Vous retirer le like de cette dedicace')
            return redirect('dedicaces')
        user.dedicaces.add(dedicace)
        Notification.objects.create(message=f'On a liker la dedicace de {dedicace.emetteur} a {dedicace.recepteur}',level='i')
        messages.info(request,'vous avez liker avec success')
        return redirect('dedicaces')


@staff_member_required
def next_prog(request):
    p=Programme.objects.filter(passe=False).order_by('rank').first()
    p.passe=True
    p.save()
    return redirect('programme')

def cadeau(request):
    return render(request,'wizard.html')

