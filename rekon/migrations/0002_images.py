# Generated by Django 3.1.1 on 2020-10-01 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='imagess')),
            ],
        ),
    ]
