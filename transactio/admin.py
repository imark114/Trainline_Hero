from django.contrib import admin
from .models import Transaction
# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['username', 'amount']

    def username(self, obj):
        return obj.account.username
