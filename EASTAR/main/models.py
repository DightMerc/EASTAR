from django.db import models

# Create your models here.


class MainPageText(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


class MainPagePhoto(models.Model):
    title = models.CharField(max_length=255)
    
    photo = models.ImageField()

    def __str__(self):
        return self.title

class TechnologiesCommonText(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


class Technologies(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title

