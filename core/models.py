from email.policy import default
from django.db import models
from django.shortcuts import reverse
import random
from django.conf import settings

def gap():
    # try:
        qq=CustomEvent.objects.get(isActive=True)
        return qq
    # except:
    #     return 0
# Create your models here.

CHOICES_LABEL=(
    ('p','primary'),
    ('s','success'),
    ('i','info'),
    ('w','warning'),
    ('d','danger')
)

CHOICES_PROG=(
    (1,'Manche'),
    (2,'Chant'),
    (3,'Jeu'),
    (4,'Slam'),
    (5,'Danse'),
    (6,'Piece de Theatre')
)

class CustomEvent(models.Model):
    titre= models.CharField(max_length=50)
    date= models.DateTimeField()
    location=models.CharField(max_length=300)
    is_concour=models.BooleanField(default=True)
    isActive=models.BooleanField()
    mc=models.CharField(max_length=50, default='Sara Casseus')

    def __str__(self) -> str:
        return f"{self.titre} -{self.date}"

    def save(self, *args, **kwargs):
        
        if self.isActive:
            for x in CustomEvent.objects.all():
                x.isActive=False
                x.save()
            self.isActive=True

        super(CustomEvent, self).save(*args, **kwargs)    

class Member(models.Model):
    nom=models.CharField(max_length=50,unique=True)
    prenom=models.CharField(max_length=50,unique=True)
    age=models.IntegerField()
    profile=models.ImageField(null=True)

    def __str__(self) -> str:
        return f"{self.nom} {self.prenom}"
    

class Concurent(models.Model):
    nom=models.CharField(max_length=50)
    pointCum=models.DecimalField(max_digits=9000,decimal_places=2,default=0)
    id_fake=models.CharField(max_length=50,default='2389A1')
    isTeam=models.BooleanField(default=False)
    coach=models.ForeignKey(Member, on_delete=models.SET_NULL,null=True,blank=True, related_name='coach')
    event= models.ForeignKey(CustomEvent,on_delete=models.SET_NULL,null=True,blank=True)
    members=models.ManyToManyField(Member)
    profile=models.ImageField(null=True)
    talent=models.DecimalField(max_digits=99,decimal_places=2,default=0)
    slogan=models.DecimalField(max_digits=99,decimal_places=2,default=0)
    otherPoint=models.DecimalField(max_digits=99,decimal_places=2,default=0)

    @property
    def isTeam(self):
        if self.members.count()>1:
            return True
        else:
            return False


    def get_vote_url(self):
        return reverse('vote', kwargs={
            "slug":self.nom
        })
    @property
    def get_nombre_votes(self):
        return fake_user.objects.filter(concurent_fav=self).count()
    @property
    def get_manches(self):
        con=[]
        for x in Manche.objects.filter(event=gap()).order_by('numero'):
            item=x.concurent.get(concurent=self)
            con.append(item)
        return con

    @property
    def position_manche(self):
        con=[]
        
        for x in Manche.objects.filter(event=gap()).order_by('numero'):
            i=1
            for y in x.get_concurent_in_order:
                if y.concurent==self:
                    con.append(i)
                    break
                i+=1
        return con

    @property
    def get_questions_posees(self):
        return Question.objects.filter(receveur=self).order_by('time_answer')

    @property
    def get_questions_repondues(self):
        return Question.objects.filter(receveur=self,repondu=True)

    @property
    def get_questions_ratees(self):
        return Question.objects.filter(receveur=self,repondu=False)

    @property
    def get_repliques(self):
        con=[]
        for x in Question.objects.filter(event=gap()):
            if self in x.repliques.all():
                con.append(x)
        return con

    @property
    def get_repliques_ratees(self):
        con=[]
        for x in Question.objects.filter(event=gap()):
            if self in x.repliques_rate.all():
                con.append(x)
        return con

    @property
    def vraiNom(self):
        if self.isTeam:
            return self.nom
        else:
            return self.members.all().first.__str__
    
    @property
    def realPoints(self):
        xx= self.pointCum + self.talent +self.slogan +self.otherPoint
        return xx

    def __str__(self) -> str:
        return self.vraiNom
    
class Concurent_par_manche(models.Model):
    concurent= models.ForeignKey(Concurent, on_delete=models.CASCADE)
    pointsCum= models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.concurent.vraiNom} - {self.pointsCum}"    

class Manche(models.Model):
    numero=models.IntegerField()
    isopen=models.BooleanField(default=True)
    event= models.ForeignKey(CustomEvent,on_delete=models.SET_NULL,null=True,blank=True)
    concurent=models.ManyToManyField(Concurent_par_manche)

    @property
    def get_concurent_in_order(self):
        concurents=self.concurent.all()
        con=sorted(concurents,key=lambda x:x.concurent.realPoints,reverse=True)        
        return con


    @property
    def get_champion_name(self):
        max=0
        concurent_max="presonne"
        for x in self.concurent.all():
            if x.concurent.realPoints > max:
                max=x.concurent.realPoints
                concurent_max= x.concurent.vraiNom
        return concurent_max

    def get_champion_points(self):
        max=0
        for x in self.concurent.all():
            if x.concurent.realPoints > max:
                max=x.concurent.realPoints
        return max


    def __str__(self) -> str:
        return f'manche #{self.numero}'   

class Dedicace(models.Model):
    emetteur=models.CharField(max_length=100)
    recepteur=models.CharField(max_length=100)
    message= models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    like_counter=models.IntegerField(default=0,editable=False)
    replique_a=models.ForeignKey("self",on_delete=models.SET_NULL,null=True,blank=True)
    show=models.BooleanField(default=False)
    event= models.ForeignKey(CustomEvent,on_delete=models.SET_NULL,null=True,blank=True)
    
    @property
    def get_nombre_likes(self):
        con=0
        users=fake_user.objects.all()
        for x in users:
            if self in x.dedicaces.all():
                con +=1
        return con       

    def get_like_url(self):
        return reverse('like', kwargs={
            "slug":self.id
        })

    def __str__(self) -> str:
        return f'De {self.emetteur} a {self.recepteur}' 

class Notification(models.Model):
    responsible= models.ForeignKey(Concurent,on_delete=models.CASCADE,null=True,blank=True)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    level=models.CharField(max_length=1,choices=CHOICES_LABEL)
    event= models.ForeignKey(CustomEvent,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.message[:25]

class Programme(models.Model):
    intervenant=models.CharField(max_length=100)
    titre=models.CharField(max_length=50)
    type=models.CharField(max_length=2)
    rank=models.IntegerField()
    passe=models.BooleanField(default=False)
    type=models.IntegerField(choices=CHOICES_PROG)
    event= models.ForeignKey(CustomEvent,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self) -> str:
        return f'{self.titre} par {self.intervenant}'

class Question(models.Model):
    enoncee=models.TextField()
    reponse=models.TextField()
    number=models.IntegerField(unique=True)
    receveur=models.ForeignKey(Concurent,null=True,blank=True,on_delete=models.SET_NULL,related_name='personne_posee')
    repondu=models.BooleanField()
    repliques= models.ManyToManyField(Concurent,related_name='persone_avoir_repondu',blank=True)
    repliques_rate=models.ManyToManyField(Concurent,blank=True)
    manche=models.ForeignKey(Manche,on_delete=models.SET_NULL,null=True,blank=True)
    used= models.BooleanField(default=False)
    time_answer=models.DateTimeField(null=True,blank=True)
    is_unique=models.BooleanField(default=False)
    is_repliques=models.BooleanField(default=True)
    is_risk=models.BooleanField(default=False)
    is_bonus=models.BooleanField(default=False)
    event= models.ForeignKey(CustomEvent,on_delete=models.SET_NULL,null=True,blank=True)


    def dump(self):
        return{
            'enoncee':self.enoncee,
            'reponse':self.reponse,
            'number':self.number,
            'is_unique':self.is_unique,
            'is_risk':self.is_risk,
            'is_repliques':self.is_repliques
        }
    def get_research_url(self):
        return reverse('get_question', kwargs={
            "slug":self.number
        })

    def __str__(self) -> str:
        return f'question #{self.number}'

class Logs(models.Model):
    concurent=models.ForeignKey(Concurent,on_delete=models.CASCADE)
    question= models.ForeignKey(Question,on_delete=models.CASCADE)
    pointsCum=models.FloatField()
    manche=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self) -> str:
        return f'{self.concurent.nom}-{self.pointsCum}'



class fake_user(models.Model):
    ip=models.CharField(max_length=100,null=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    concurent_fav=models.ForeignKey(Concurent,on_delete=models.SET_NULL,null=True,blank=True)
    dedicaces=models.ManyToManyField(Dedicace)
    default_name=models.CharField(max_length=2000,default='Annonyme')
    
    
    def __str__(self) -> str:
        try:
         return f'{self.user.username}'
        except:
            return f'Anonymous_user{self.id}'


class cadeau(models.Model):
    nombre_disponible=models.IntegerField()
    cadeau=models.TextField()
    show=models.BooleanField(default=False)
    event= models.ForeignKey(CustomEvent,on_delete=models.SET_NULL,null=True,blank=True)

    @property
    def winners(self):
        return order.objects.filter(cadeau=self)
    @property
    def is_open(self):
        if order.objects.filter(cadeau=self).count() < self.nombre_disponible:
            return True
        else:
            return False
    

    def __str__(self):
        return self.cadeau[:24]

    def save(self, *args, **kwargs):
        if self.show:
            for x in cadeau.objects.filter(event=gap()):
                x.show=False
                x.save()
            self.show=True        
        super(cadeau, self).save(*args, **kwargs)
    

class cadeau_quesion(models.Model):
    cadeau=models.ForeignKey(cadeau,on_delete=models.CASCADE,related_name='qsts')
    libelle=models.TextField()
    reponse_true=models.TextField()
    reponse_fake_1=models.TextField()
    reponse_fake_2=models.TextField()
    reponse_fake_3=models.TextField()
    event= models.ForeignKey(CustomEvent,on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self):
        return self.libelle[:25]

    @property
    def list_reponse(self):
        y=[self.reponse_fake_3,self.reponse_fake_2,self.reponse_fake_1,self.reponse_true]
        random.shuffle(y)
        return y

class order(models.Model):
    cadeau=models.ForeignKey(cadeau,on_delete=models.CASCADE)
    user=models.ForeignKey(fake_user,on_delete=models.CASCADE)
    is_redeem=models.BooleanField(default=False)
    event=models.ForeignKey(CustomEvent,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'{self.user}-{self.cadeau}'
