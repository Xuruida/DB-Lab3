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
    contact_name = models.CharField(max_length=30)
    contact_tel = models.CharField(max_length=30)
    contact_email = models.EmailField()
    relation = models.CharField(max_length=20)

    def __str__(self):
        return '%s, %s' % (self.name, self.ID_number)

class ClientStaff(models.Model):
    """
    Relation between Client and Staff.
    Fields: client, staff, relation_type
    Constraints: Unique(client, staff, relation_type)
    """

    client = models.ForeignKey('ClientInfo', on_delete=models.CASCADE)
    staff = models.ForeignKey('branch.StaffInfo', on_delete=models.CASCADE)

    relation_type = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['client', 'staff', 'relation_type'],
                name='unique_cl_st'
            )
        ]

    def __str__(self):
        return '%s, %s, %s' % (self.client, self.staff, self.relation_type)