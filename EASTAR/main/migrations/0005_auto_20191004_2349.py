# Generated by Django 2.2.6 on 2019-10-04 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_technologies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField(verbose_name='Описание')),
                ('photo', models.ManyToManyField(to='main.PagePhoto')),
            ],
        ),
        migrations.DeleteModel(
            name='TechnologiesText',
        ),
    ]
