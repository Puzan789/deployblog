# Generated by Django 4.1.7 on 2023-02-15 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
