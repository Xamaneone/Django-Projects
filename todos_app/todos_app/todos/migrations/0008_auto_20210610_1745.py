# Generated by Django 3.2.4 on 2021-06-10 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0007_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Work', 'Work stuff'), ('Home', 'Home stuff')], max_length=20),
        ),
    ]
