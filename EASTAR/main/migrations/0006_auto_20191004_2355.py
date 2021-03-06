# Generated by Django 2.2.6 on 2019-10-04 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191004_2349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contenttext',
            old_name='title',
            new_name='titleEN',
        ),
        migrations.RenameField(
            model_name='technologies',
            old_name='title',
            new_name='titleEN',
        ),
        migrations.RenameField(
            model_name='technologiesmoretext',
            old_name='title',
            new_name='titleEN',
        ),
        migrations.RemoveField(
            model_name='contenttext',
            name='text',
        ),
        migrations.RemoveField(
            model_name='technologies',
            name='text',
        ),
        migrations.RemoveField(
            model_name='technologiesmoretext',
            name='text',
        ),
        migrations.AddField(
            model_name='contenttext',
            name='textEN',
            field=models.TextField(default=None, verbose_name='Текст EN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contenttext',
            name='textRU',
            field=models.TextField(default=None, verbose_name='Текст RU'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contenttext',
            name='textUZ',
            field=models.TextField(default=None, verbose_name='Текст UZ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contenttext',
            name='titleRU',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contenttext',
            name='titleUZ',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technologies',
            name='textEN',
            field=models.TextField(default=None, verbose_name='Описание EN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technologies',
            name='textRU',
            field=models.TextField(default=None, verbose_name='Описание RU'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technologies',
            name='textUZ',
            field=models.TextField(default=None, verbose_name='Описание UZ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technologies',
            name='titleRU',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technologies',
            name='titleUZ',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technologiesmoretext',
            name='textEN',
            field=models.TextField(default=None, verbose_name='Текст EN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technologiesmoretext',
            name='textRU',
            field=models.TextField(default=None, verbose_name='Текст RU'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technologiesmoretext',
            name='textUZ',
            field=models.TextField(default=None, verbose_name='Текст UZ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technologiesmoretext',
            name='titleRU',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technologiesmoretext',
            name='titleUZ',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
