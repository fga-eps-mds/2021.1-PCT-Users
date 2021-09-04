from django.db import models

class SavedSearch(models.Model):
    search_text = models.CharField("Url", max_length=1024)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
