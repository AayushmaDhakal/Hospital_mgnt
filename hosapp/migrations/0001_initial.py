# Generated by Django 4.2.3 on 2024-04-01 14:37

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Is admin')),
                ('is_doctor', models.BooleanField(default=False, verbose_name='Is doctor')),
                ('is_patient', models.BooleanField(default=False, verbose_name='Is patient')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is staff')),
                ('Approve', models.BooleanField(default=False, verbose_name='Approve')),
                ('Appoint', models.BooleanField(default=False, verbose_name='Appoint')),
                ('Discharge', models.BooleanField(default=False, verbose_name='Discharge')),
                ('username', models.CharField(max_length=70, unique=True)),
                ('pFname', models.CharField(max_length=70, null=True)),
                ('pLname', models.CharField(max_length=70, null=True)),
                ('dFname', models.CharField(max_length=70, null=True)),
                ('dLname', models.CharField(max_length=70, null=True)),
                ('stf_Fname', models.CharField(max_length=70, null=True)),
                ('stf_Lname', models.CharField(max_length=70, null=True)),
                ('Dphone', models.IntegerField(null=True)),
                ('dob', models.DateField(null=True)),
                ('Admit_date', models.DateField(null=True)),
                ('Discharge_date', models.DateField(null=True)),
                ('phone', models.IntegerField(null=True)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('password', models.CharField(max_length=70)),
                ('address', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=100, null=True)),
                ('Ailment', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
                ('Problem_pat', models.CharField(max_length=1000, null=True)),
                ('roomcharge', models.IntegerField(null=True)),
                ('doctorcharge', models.IntegerField(null=True)),
                ('medicinecharge', models.IntegerField(null=True)),
                ('othercharge', models.IntegerField(null=True)),
                ('totalcharge', models.IntegerField(null=True)),
                ('cardiovascular', models.CharField(max_length=1000, null=True)),
                ('Pulmonary', models.CharField(max_length=1000, null=True)),
                ('Gastroenterology', models.CharField(max_length=1000, null=True)),
                ('Neurology', models.CharField(max_length=1000, null=True)),
                ('Musculoskeleton', models.CharField(max_length=1000, null=True)),
                ('Gentiourinary', models.CharField(max_length=1000, null=True)),
                ('Oro', models.CharField(max_length=1000, null=True)),
                ('Extremities', models.CharField(max_length=1000, null=True)),
                ('Hernia', models.CharField(max_length=1000, null=True)),
                ('Hydrocele', models.CharField(max_length=1000, null=True)),
                ('Varicose', models.CharField(max_length=1000, null=True)),
                ('Eyeright', models.CharField(max_length=1000, null=True)),
                ('Eyeleft', models.CharField(max_length=1000, null=True)),
                ('Earright', models.CharField(max_length=1000, null=True)),
                ('Earleft', models.CharField(max_length=1000, null=True)),
                ('other', models.CharField(max_length=1000, null=True)),
                ('chestxray', models.CharField(max_length=1000, null=True)),
                ('impression', models.CharField(max_length=1000, null=True)),
                ('rbc', models.CharField(max_length=1000, null=True)),
                ('plus', models.CharField(max_length=1000, null=True)),
                ('epithelial', models.CharField(max_length=1000, null=True)),
                ('pregnancy', models.CharField(max_length=1000, null=True)),
                ('wbc', models.CharField(max_length=1000, null=True)),
                ('Neutrophils', models.CharField(max_length=1000, null=True)),
                ('Lymphocytes', models.CharField(max_length=1000, null=True)),
                ('Eosinophils', models.CharField(max_length=1000, null=True)),
                ('monocytes', models.CharField(max_length=1000, null=True)),
                ('basophils', models.CharField(max_length=1000, null=True)),
                ('hemoglobin', models.CharField(max_length=1000, null=True)),
                ('malaria', models.CharField(max_length=1000, null=True)),
                ('filaria', models.CharField(max_length=1000, null=True)),
                ('sugar', models.CharField(max_length=1000, null=True)),
                ('urea', models.CharField(max_length=1000, null=True)),
                ('creatine', models.CharField(max_length=1000, null=True)),
                ('bilirubin', models.CharField(max_length=1000, null=True)),
                ('sgpt', models.CharField(max_length=1000, null=True)),
                ('scot', models.CharField(max_length=1000, null=True)),
                ('hiv', models.CharField(max_length=1000, null=True)),
                ('hbsag', models.CharField(max_length=1000, null=True)),
                ('vdrl', models.CharField(max_length=1000, null=True)),
                ('tpha', models.CharField(max_length=1000, null=True)),
                ('bloodgroup', models.CharField(max_length=1000, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
