from django.db import models

from products.models import Product


# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])

#     def __str__(self):
#         return f"Order {self.id} - {self.user.username}"
