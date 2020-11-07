from django.db import models




class Bid(models.Model):

    text = models.TextField()
    date = models.DateTimeField(auto_now = True)
    responsible = models.ForeignKey('Responsible', on_delete=models.CASCADE)
    client = models.ForeignKey('Client',  on_delete=models.CASCADE)


class Client(models.Model):
    fio = models.TextField(max_length=130)
    number = models.TextField(max_length=30)


class Responsible(models.Model):
    fio = models.TextField(max_length=120)
    position = models.TextField(max_length=120)



# Create your models here.
