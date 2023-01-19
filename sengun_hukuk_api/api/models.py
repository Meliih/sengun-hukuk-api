from django.db import models

# Create your models here.

class User(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    tc=models.BigIntegerField()
    email=models.CharField(max_length=50)
    birth_date=models.DateTimeField()
    phone=models.BigIntegerField()
    password=models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'User'
    def __str__(self):
        return self.name

class Dava(models.Model):
    id=models.AutoField(primary_key=True)
    raf_no=models.CharField(max_length=50)
    arsiv_no=models.IntegerField()
    davaci=models.IntegerField()
    davali=models.IntegerField()
    yer=models.CharField(max_length=50)
    daire=models.CharField(max_length=40)
    mahkeme=models.CharField(max_length=100)
    dosya_esas=models.CharField(max_length=50)
    konu=models.CharField(max_length=100)
    durusma_gunu =models.DateTimeField()
    acik_kapali=models.CharField(max_length=30)
    karar =models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Dava'
        verbose_name_plural = 'Dava'
    def __str__(self):
        return self.raf_no

class Davaci(models.Model):
    id=models.AutoField(primary_key=True)
    dava_id = models.IntegerField()
    davaci_id = models.IntegerField()
   
    class Meta:
        verbose_name = 'Davaci'
        verbose_name_plural = 'Davaci'
    def __str__(self):
        return str(self.davaci_id)

class Icra(models.Model):
    id=models.AutoField(primary_key=True)
    arsiv=models.IntegerField()
    raf_no=models.IntegerField()
    alacakli=models.IntegerField()
    borclu=models.IntegerField()
    yer=models.CharField(max_length=50)
    daire=models.CharField(max_length=75)
    dosya_esas=models.CharField(max_length=80)
    konu=models.CharField(max_length=100)
    acilis_tarihi=models.DateTimeField()
    tebligat_durumu=models.CharField(max_length=70)
    son_islem_tarihi=models.DateTimeField()
    durum=models.CharField(max_length=32)
    class Meta:
        verbose_name = 'Icra'
        verbose_name_plural = 'Icra'
    def __str__(self):
        return self.raf_no



class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=128)
    date=models.DateTimeField()
    priority=models.IntegerField()
    color=models.IntegerField()
    description=models.CharField(max_length=256)
    class Meta:
        verbose_name = 'Notes'
        verbose_name_plural = 'Notes'
    def __str__(self):
        return self.title
class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    eventName=models.CharField(max_length=72)
    startdate=models.DateTimeField()
    enddate=models.DateTimeField()
    background=models.CharField(max_length=24)
    isallDay=models.BooleanField()
    description=models.CharField(max_length=128)
    class Meta:
        verbose_name = 'Appointments'
        verbose_name_plural = 'Appointments'
    def __str__(self):
        return self.title 

class OurService(models.Model):
    id = models.AutoField(primary_key=True)
    header = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    img = models.CharField(max_length=256)
    time = models.DateTimeField()
    department = models.IntegerField()
    class Meta:
        verbose_name = 'OurServices'
        verbose_name_plural = 'OurServices'
    def __str__(self):
        return self.header

class ArticleAndNew(models.Model):
    id = models.AutoField(primary_key=True)
    header = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    img = models.CharField(max_length=256)
    time = models.DateTimeField()
    department = models.IntegerField()
    class Meta:
        verbose_name = 'ArticleAndNews'
        verbose_name_plural = 'ArticleAndNews'
    def __str__(self):
        return self.header

class Lawyer(models.Model):
    id = models.AutoField(primary_key=True) 
    identitynumber = models.BigIntegerField()
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    img = models.CharField(max_length=256)
    role = models.CharField(max_length=32)
    content = models.CharField(max_length=512)
    birth_date=models.DateTimeField()
    class Meta:
        verbose_name = 'Lawyer'
        verbose_name_plural = 'Lawyer'
    def __str__(self):
        return self.name

class Reference(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=256)
    class Meta:
        verbose_name = 'Reference'
        verbose_name_plural = 'Reference'
    def __str__(self):
        return self.image