from django.db import models

from account.entity.account import Account
from django.utils import timezone

from foodorders.entity.foodorders_status import FoodorderStatus


class Foodorders(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='foodorders')
    status = models.CharField(max_length=10, choices=FoodorderStatus.choices, default=FoodorderStatus.PENDING)
    created_date = models.DateTimeField(default=timezone.now)
    # total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # shipping_address = models.CharField(max_length=255)
    # billing_address = models.CharField(max_length=255)

    def __str__(self):
        return f"Foodorders {self.id} by {self.account}"

    class Meta:
        db_table = 'foodorders'
        app_label = 'foodorders'
