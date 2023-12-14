
from django.db import models


# Create your models here.

status_choice= [ 
    ('SCUBE', 'SCUBE'),
    ('GODOWN', 'GODOWN'),
    ('SALE', 'SALE'),
    ('ORDER','ORDER')
]

Catogory_choice= [ 
    ('CUPBOARD', 'CUPBOARD'),
    ('TABLE', 'TABLE'),
    ('BEDROOM-SET', 'BEDROOM-SET'),
    ('POOJA-STAND','POOJA-STAND'),
    ('TV-STAND','TV-STAND'),
    ('SOFA','SOFA'),
    ('OTHERS','OTHERS'),
    ('ORDER','ORDER'),
    
]



class Scube_ss(models.Model):
    code=models.CharField(max_length=50 ,null=True)
    Catogory= models.CharField(choices=Catogory_choice , max_length=50 ,null=True )
    name=models.CharField(max_length=50 ,null=True)
    size=models.CharField(null=True,blank=True)
    prize=models.IntegerField(null=True,blank=True)
    material=models.CharField(null=True)
    color=models.CharField(null=True,blank=True)
    pr_date=models.DateField(null=True)
    sl_date=models.DateField(null=True, blank=True)
    status= models.CharField(choices=status_choice , max_length=50 ,null=True )
    image=models.ImageField(upload_to='images/',blank=True)

class orders(models.Model):
    name=models.CharField(max_length=50 ,null=True,)
    size=models.CharField(null=True,blank=True)
    color=models.CharField(null=True,blank=True)
    image=models.ImageField(upload_to='images/',blank=True)
    details=models.CharField(max_length=150 ,null=True, blank=True)    
