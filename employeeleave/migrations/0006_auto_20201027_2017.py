# Generated by Django 3.0.3 on 2020-10-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeleave', '0005_auto_20201027_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaves',
            name='adminremark',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='adminremarkdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
