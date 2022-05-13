# Generated by Django 4.0.4 on 2022-05-12 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_preference'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='preference',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='preference',
            name='date',
            field=models.DateField(verbose_name='preference date'),
        ),
    ]