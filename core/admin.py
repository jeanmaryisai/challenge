from django.contrib import admin
from .models import *
# Register your models here.
class dedicace(admin.ModelAdmin):
    list_display= [
        'emetteur',
        'recepteur',
        'like_counter',
        "show"

    ]
    list_editable=['show']
    list_filter=[
        'show',
        'event'
        
    ]

class programe(admin.ModelAdmin):
    list_display=[
        'titre',
        'rank',
        'passe',
    ]
    list_editable=['passe','rank']
    list_filter=[
        'passe',
        'event'
    ]
    ordering=['rank']

class question(admin.ModelAdmin):
    list_display=['number','manche','used']
    list_filter=['used',
        'event']
    ordering=['manche']

class concurentAdmin(admin.ModelAdmin):
    list_filter=[
        'event']




admin.site.register(Concurent,concurentAdmin)
admin.site.register(Manche,list_filter=['event'])
admin.site.register(Dedicace,dedicace)
admin.site.register(Notification,list_filter=['event'])
admin.site.register(Programme,programe)
admin.site.register(Question,question)
admin.site.register(Concurent_par_manche)
admin.site.register(Logs)
admin.site.register(fake_user)
admin.site.register(cadeau,list_filter=['event'])
admin.site.register(cadeau_quesion,list_filter=['event'])
admin.site.register(order)
admin.site.register(CustomEvent,list_filter=['date'])
admin.site.register(Member)





