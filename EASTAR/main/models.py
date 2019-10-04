from django.db import models

# Create your models here.


class MainPagePhoto(models.Model):
    title = models.CharField(max_length=255)
    
    photo = models.ImageField()

    def __str__(self):
        return self.title


class PagePhoto(models.Model):
    title = models.CharField(max_length=255)
    
    photo = models.ImageField()

    def __str__(self):
        return self.title


class ContentText(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


class TechnologiesText(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


class TechnologiesMoreText(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title
