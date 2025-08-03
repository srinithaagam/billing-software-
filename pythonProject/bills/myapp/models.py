# from django.db import models
#
# # Create your models here.
# from django.db import models
#
# # class Item(models.Model):
# #     material = models.CharField(max_length=100)
# #     quantity = models.FloatField()  # in kg
# #     rate = models.FloatField()      # Rs per kg
# #
# #     @property
# #     def total(self):
# #         return self.quantity * self.rate
# from django.db import models
# # import uuid
# #
# # class Item(models.Model):
# #     bill_id = models.UUIDField(default=uuid.uuid4, editable=False)
# #     customer_name = models.CharField(max_length=100)
# #     material = models.CharField(max_length=100)
# #     quantity = models.FloatField()
# #     rate = models.FloatField()
# #
# #     @property
# #     def total(self):
# #         return self.quantity * self.rate
# # from django.db import models
# # import uuid
# #
# # class Item(models.Model):
# #     bill_id = models.UUIDField()
# #     customer_name = models.CharField(max_length=100)
# #     material = models.CharField(max_length=100)
# #     quantity = models.FloatField()
# #     rate = models.FloatField()
# #
# #     @property
# #     def total(self):
# #         return self.quantity * self.rate
# from django.db import models
# import uuid
#
# from bills.myapp.views import Bill
#
# #
# # class Item(models.Model):
# #     bill_id = models.UUIDField()  # unique ID per bill/session
# #     customer_name = models.CharField(max_length=100)
# #     material = models.CharField(max_length=100)
# #     quantity = models.FloatField()
# #     rate = models.FloatField()
# #
# #     @property
# #     def total(self):
# #         return self.quantity * self.rate
# #
# #     def __str__(self):
# #         return f"{self.material} - {self.quantity}kg @ Rs{self.rate}/kg"
# class Item(models.Model):
#     bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='items')
#     customer_name = models.CharField(max_length=100)
#     material = models.CharField(max_length=100)
#     quantity = models.FloatField()
#     rate = models.FloatField()
#
#     @property
#     def total(self):
#         return self.quantity * self.rate
#
#     def __str__(self):
#         return f"{self.material} - {self.quantity}kg @ Rs{self.rate}/kg"
#
from django.db import models


# class Bill(models.Model):
#     bill_number = models.CharField(max_length=20, unique=True, blank=True)
#     customer_name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.formatted_bill_number()} - {self.customer_name}"
#
#     def formatted_bill_number(self):
#         return f"BILL-{self.id:03d}"  # Example: BILL-001
class Bill(models.Model):
    bill_number = models.CharField(max_length=20, unique=True, blank=True)
    customer_name = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.bill_number:
            last = Bill.objects.all().order_by('id').last()
            num = last.id + 1 if last else 1
            self.bill_number = f"BILL-{num:03d}"
        super().save(*args, **kwargs)

class Item(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='items')
    material = models.CharField(max_length=255)
    quantity = models.FloatField()
    rate = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return f"{self.material} - {self.total:.2f}"

