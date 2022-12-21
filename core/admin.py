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
        'show'
    ]

class programe(admin.ModelAdmin):
    list_display=[
        'titre',
        'rank',
        'passe',
    ]
    list_editable=['passe','rank']
    list_filter=[
        'passe'
    ]
    ordering=['rank']

class question(admin.ModelAdmin):
    list_display=['number','manche','used']
    list_filter=['used']
    ordering=['manche']

admin.site.register(Concurent)
admin.site.register(Manche)
admin.site.register(Dedicace,dedicace)
admin.site.register(Notification)
admin.site.register(Programme,programe)
admin.site.register(Question,question)
admin.site.register(Concurent_par_manche)
admin.site.register(Logs)
admin.site.register(fake_user)
