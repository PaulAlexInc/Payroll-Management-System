# Generated by Django 3.1.3 on 2021-01-26 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0009_auto_20210109_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary_mgmt',
            name='id',
        ),
        migrations.AlterField(
            model_name='salary_mgmt',
            name='AC_No',
            field=models.CharField(default='None', max_length=200, primary_key=True, serialize=False),
        ),
    ]
