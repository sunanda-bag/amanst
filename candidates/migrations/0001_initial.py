# Generated by Django 3.2.3 on 2021-06-04 20:11

import candidates.models
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email_id', models.CharField(blank=True, max_length=100, null=True)),
                ('Years_of_Experience', models.DecimalField(blank=True, decimal_places=0, default=None, max_digits=1, null=True)),
                ('Linkedin_Profile', models.CharField(max_length=100, null=True)),
                ('Expected_hourly_rate', models.DecimalField(blank=True, decimal_places=0, default=None, max_digits=2, null=True)),
                ('Resume', models.FileField(upload_to='doc', validators=[candidates.models.file_size])),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('req_id', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Req_Id', models.IntegerField()),
                ('Job_title', models.CharField(max_length=255)),
                ('Start_date', models.DateField()),
                ('End_date', models.DateField()),
                ('Submission_deadline', models.DateTimeField()),
                ('No_Openings', models.IntegerField()),
                ('Description', ckeditor_uploader.fields.RichTextUploadingField(default='')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.location')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.role')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateJobMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=30)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.candidate')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.job')),
            ],
            options={
                'verbose_name_plural': 'All_Candidates',
            },
        ),
    ]
