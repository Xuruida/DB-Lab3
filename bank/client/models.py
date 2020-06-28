from django.db import models

# Create your models here.

class ClientInfo(models.Model):
    """
    Client Information.
    Fields: ID_number, name, tel, address, contact, relation
    """

    ID_number = models.CharField(max_length=18, primary_key=True)
    name = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    contact = models.ForeignKey('ContactInfo', on_delete=models.SET_NULL)
    relation = models.CharField(max_length=20)

    def __str__(self):
        return '%s, %s' % (name, ID_number)

class ContactInfo(models.Model):
    """
    Contact Information.
    Fields: name, tel, email
    """

    name = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return '%s' % name