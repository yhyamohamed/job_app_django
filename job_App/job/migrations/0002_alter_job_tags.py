# Generated by Django 4.0.4 on 2022-06-14 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_user_type'),
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='tags',
            field=models.ManyToManyField(blank=True, to='accounts.tag'),
        ),
    ]