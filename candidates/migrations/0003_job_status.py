# Generated by Django 3.2.3 on 2021-06-06 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_alter_job_req_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
