# Generated by Django 4.2.2 on 2023-06-25 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0002_alter_profileclient_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileclient',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'APROVADO'), (2, 'NEGADO'), (0, 'PENDING')], default=0, null=True),
        ),
    ]
