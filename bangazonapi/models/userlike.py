from django.db import models
from .customer import Customer


class UserLike(models.Model):

    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="liked")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    

