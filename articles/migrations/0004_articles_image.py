# Generated by Django 4.1.5 on 2023-01-02 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articles_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='article', verbose_name='عکس مقاله'),
        ),
    ]
