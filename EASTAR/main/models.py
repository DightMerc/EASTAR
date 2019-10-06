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
    titleRU = models.CharField(max_length=255)
    titleUZ = models.CharField(max_length=255)
    titleEN = models.CharField(max_length=255)

    textRU = models.TextField("Текст RU")
    textUZ = models.TextField("Текст UZ")
    textEN = models.TextField("Текст EN")

    def __str__(self):
        return self.titleRU


class Technologies(models.Model):
    titleRU = models.CharField(max_length=255)
    titleUZ = models.CharField(max_length=255)
    titleEN = models.CharField(max_length=255)

    textRU = models.TextField("Описание RU")
    textUZ = models.TextField("Описание UZ")
    textEN = models.TextField("Описание EN")
    
    textAddRU = models.TextField("Дополнительный текст RU")
    textAddUZ = models.TextField("Дополнительный текст UZ")
    textAddEN = models.TextField("Дополнительный текст EN")

    photo = models.ManyToManyField(PagePhoto)

    def __str__(self):
        return self.titleRU
