# Generated by Django 4.1.7 on 2023-07-16 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_mapping'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='painting',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='mapping',
            name='image',
            field=models.ImageField(null=True, upload_to='mapping/'),
        ),
        migrations.AddField(
            model_name='mapping',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='painting',
            name='text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]