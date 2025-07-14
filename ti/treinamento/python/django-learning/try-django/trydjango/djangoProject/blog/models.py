from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title   = models.CharField(max_length=120)
    content = models.TextField()
    active  = models.BooleanField(default=False, null=True, blank=True)

    def articles_links(self):
        return reverse("articles:articles-details", kwargs={'id':self.id})
    
    def articles_update(self):
        return reverse("articles:articles-update", kwargs={'id':self.id})
    
    def articles_delete(self):
        return reverse("articles:articles_delete", kwargs={'id':self.id})

