from django.db import models
from train.models import Train
from account.models import User

# Create your models here.
class BookedSeat(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    balance_after_buy = models.DecimalField(decimal_places=2, max_digits=12)

class Comment(models.Model):
    train = models.ForeignKey(Train,on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)