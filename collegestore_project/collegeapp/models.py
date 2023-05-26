from django.db import models
from django.urls import reverse


# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    url=models.TextField(blank=True)
    #image=models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'

    def get_url(self):
        return reverse('collegeapp:departments',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Course(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    dept = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        ordering=('name',)
        verbose_name='course'
        verbose_name_plural='courses'

  #  def get_url(self):
   #     return reverse('shop:prodCatdetail',args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Material(models.Model):
    uid = models.CharField(max_length=250)
    dob = models.DateField(max_length=250)
    age = models.IntegerField()
    gen = models.CharField(max_length=250)
    ph = models.CharField(max_length=250, unique=True)
    mail = models.TextField(blank=True,unique=True)
    add = models.TextField(blank=True)
    dept = models.CharField(max_length=250)
    cou = models.CharField(max_length=250)
    pur = models.CharField(max_length=250)
    mat = models.CharField(max_length=250)


    class Meta:
        #ordering=(*)
        verbose_name='material'
        verbose_name_plural='materials'

  #  def get_url(self):
   #     return reverse('shop:prodCatdetail',args=[self.category.slug,self.slug])


