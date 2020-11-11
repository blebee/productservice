from django.db import models

# Create your models here.

class tbsafelog(models.Model):
    slgsn= models.CharField(max_length=50)
    slgcputype =models.CharField(max_length=50)
    slgcliamin = models.DateField()
    slgcliamout = models.DateField()
    slgdesc = models.TextField()
    admit = models.DateField(null=True)
    slgtype_choices = (
        ('J1900','1900'),
        ('Corei5','Corei5'),
    )
    slgtpye = models.CharField(max_length=30, blank=True, null=True, choices=slgtype_choices)


class tbups(models.Model):
    upssn = models.CharField(max_length=50)
    upsadmitdate = models.DateField()
    upstype_choices = (
        ('850V','850V'),
        ('1000V','1000V'),
        ('1200V','1200'),
    )
    upstype = models.CharField(max_length=30, blank=True, null= True, choices=upstype_choices)
    description = models.TextField()

class tbcustomer(models.Model):
    cusname = models.CharField(max_length=100)
    custel = models.CharField(max_length=30)
    cusaddress= models.CharField(max_length=100)
    cusdes= models.TextField()

class tblli(models.Model):
    lli = models.CharField(max_length=10)
    lliip = models.CharField(max_length=50)
    llides = models.TextField()

class tbfttx(models.Model):
    fttx = models.CharField(max_length=10)
    fttxdes = models.TextField()
 

