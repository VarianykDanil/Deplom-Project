# Generated by Django 4.1.7 on 2023-06-18 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FileApp', '0006_alter_file_category_alter_file_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='description',
            field=models.TextField(default='Опису нема'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_path',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='files/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(default='Безіменний файл', max_length=255),
        ),
        migrations.AlterField(
            model_name='file',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]