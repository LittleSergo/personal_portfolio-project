# Generated by Django 4.1.2 on 2022-11-16 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_discription_alter_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='last_change',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(),
        ),
    ]
