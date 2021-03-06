# Generated by Django 2.2.3 on 2019-07-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_auto_20190722_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='no_user_favourites',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quote',
            name='no_user_likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quote',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
