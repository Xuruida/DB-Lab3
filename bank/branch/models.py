from django.db import models

# Create your models here.

class BranchInfo(models.Model):
    """
    Branch Information.
    Fields: name, city
    Constraints: Unique(name)
    """

    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name'],
                name='unique_branch_name'
            )
        ]
        
    def __str__(self):
        return '%s, %s' % (name, city)


class StaffInfo(models.Model):
    """
    Staff Information.
    Fields: ID_number, name, tel, address, entry_date
    Constraints: Unique(ID_number)
    """

    ID_number = models.CharField(max_length=18, primary_key=True)
    name = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    entry_date = models.DateField()

    def __str__(self):
        return '%s, %s' % (name, ID_number)

class DepartmentInfo(models.Model):
    """
    Department Information.
    Fields: department_ID, name, type, branch, manager.
    """

    dep_ID = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=30)
    dep_type = models.IntegerField()
    branch = models.ForeignKey('BranchInfo', on_delete=models.CASCADE)
    manager = models.ForeignKey('StaffInfo', on_delete=models.SET_NULL)

    def __str__(self):
        return '%s, %s, %s' % (name, dep_ID, branch)