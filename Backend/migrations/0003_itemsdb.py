# Generated by Django 5.0 on 2023-12-19 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_rename_caegoryimage_categorydb_categoryimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='itemsdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemCategory', models.CharField(blank=True, max_length=100, null=True)),
                ('ItemName', models.CharField(blank=True, max_length=100, null=True)),
                ('ItemPrice', models.IntegerField(blank=True, null=True)),
                ('Image1', models.ImageField(blank=True, null=True, upload_to='Item Images')),
                ('Image2', models.ImageField(blank=True, null=True, upload_to='Item Images')),
                ('ItemDescription', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
