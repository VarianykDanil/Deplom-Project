# Generated by Django 4.1.7 on 2023-06-24 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SubscriptionApp', '0002_subscription_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='size',
            field=models.IntegerField(default=0),
        ),
    ]