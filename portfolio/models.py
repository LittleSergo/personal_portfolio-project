from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/')
    last_change = models.DateField(auto_now=True)
    date = models.DateField()

    def __str__(self):
        return self.title
