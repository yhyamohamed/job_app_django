# Generated by Django 4.0.5 on 2022-06-18 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='cvs/%Y'),
        ),
    ]
