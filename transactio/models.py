from django.db import models
from account.models import User

# Create your models here.
class Transaction(models.Model):
    account = models.ForeignKey(User,related_name='transactions',on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    def __str__(self):
        return self.account.username