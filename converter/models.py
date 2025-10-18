from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

class Conversion(models.model):
    user = models.ForeignKey(user, null=True, blank=True, on_delete=models.SET_NULL)
    from_currency = models.charField(max_length=10)
    to_currency = models.CharField(max_length=10)
    amount = models.decimalField(max_digits=20, decimal_places=6)
    result = models.DecimalField(max_digits=20, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.amount} {self.from_currency} -> {self.result} {self.to_currency}"
    

