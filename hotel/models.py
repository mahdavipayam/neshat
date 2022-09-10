from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Users(models.Model):
    FierstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    FatherName = models.CharField(max_length=30)
    NationalCode = models.IntegerField(null=True)
    Age = models.IntegerField(null=True)
    PhoneNumber = models.IntegerField(null=True)
    Adress = models.TextField(null=True)


class Rooms(models.Model):
    ROOM_TYPE       =(('twins','تویین'),('double','دوبل'),('oneroom','تک اتاقه'),('towroom','دو اتاقه'))
    AGENT_NAME      =(('snaproom', 'اسنپ روم'),('jabama', 'جاباما'),('otaghak',' اتاقک'),('lamaso','لاماسو'))
    RELATE_TYPRE   =(('family1', 'بستگان درجه1'),('family2', 'بستگان درجه2'),('freind',' دوست'),('coworker','همراه'),('1','1'))


    UserGuest   = models.ManyToManyField(Users)
    Number = models.CharField(max_length=3 ,null=True)
    EnterDate = models.DateTimeField(auto_now_add=True)
    Eghamat  =  models.IntegerField(null=True)
    TypeRoom = models.CharField(max_length=10, choices=ROOM_TYPE)
    AgentName = models.CharField(max_length=20, choices=AGENT_NAME )


    Relatelastname1         = models.CharField(max_length=20, default='null')
    Relatename1             = models.CharField(max_length=20, default='null')
    Relatetype1             =models.CharField(max_length=20 , null=True, choices=RELATE_TYPRE,default='1' )

    Relatename2             = models.CharField(max_length=20, default='null')
    Relatelastname2         = models.CharField(max_length=20, default='null')
    Relatetype2             =models.CharField(max_length=20 , null=True, choices=RELATE_TYPRE, default='1')

    Relatename3             = models.CharField(max_length=20, default='null')
    Relatelastname3         = models.CharField(max_length=20, default='null')
    Relatetype3             =models.CharField(max_length=20, null=True, choices=RELATE_TYPRE, default='1')

    def __str__(self):
        return self.Number

