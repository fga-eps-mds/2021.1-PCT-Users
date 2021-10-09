from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=240)
    email = models.CharField(max_length=240)
    password = models.CharField(max_length=240)
    isDeleted = models.BooleanField(default=False)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name