from django.db import models
from django.contrib.auth import get_user_model


class Drums(models.Model):
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name_plural = 'Drums'
