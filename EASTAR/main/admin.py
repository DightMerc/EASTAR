from django.contrib import admin
from .models import MainPagePhoto, PagePhoto, ContentText, TechnologiesMoreText, TechnologiesText
# Register your models here.


admin.site.register(MainPagePhoto)
admin.site.register(PagePhoto)
admin.site.register(ContentText)
admin.site.register(TechnologiesMoreText)
admin.site.register(TechnologiesText)
