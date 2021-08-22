from django.db import models

CATEGORY = (('all', '全員'), ('limited', '会員限定'))

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    content = models.TextField()
    category = models.CharField(
        max_length=50, 
        choices=CATEGORY)
    
    def __str__(self):
        return self.title