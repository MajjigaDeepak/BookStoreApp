from django.db import models

# Create your models here.


class authors(models.Model):

    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name

class books(models.Model):

    id=models.AutoField(primary_key=True)
    authorName=models.ForeignKey(authors)
    bookName = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.bookName

class orders(models.Model):

    id=models.AutoField(primary_key=True)
    bought = models.ForeignKey(books)
    customerName=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.customerName



