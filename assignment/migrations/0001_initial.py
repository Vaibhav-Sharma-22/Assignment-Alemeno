# Generated by Django 4.0.3 on 2022-03-21 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Kid_Name', models.CharField(max_length=100, verbose_name='Name')),
                ('Kid_Age', models.IntegerField(verbose_name='Age')),
                ('Parent_Phone_Number', models.IntegerField(blank=True)),
                ('Parent_Email_Address', models.EmailField(max_length=254, verbose_name='Email Address')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image_URL', models.URLField()),
                ('Created_On', models.DateTimeField()),
                ('Updated_on', models.DateTimeField()),
                ('Is_Approved', models.BooleanField()),
                ('Approved_by', models.CharField(max_length=50, verbose_name='')),
                ('Kid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assignment.kid')),
            ],
        ),
    ]
