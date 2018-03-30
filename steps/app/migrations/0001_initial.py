# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-30 05:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.CharField(choices=[('Mob', 'Mobile No.'), ('Email', 'Email')], max_length=10, verbose_name='Contact Type')),
                ('value', models.TextField()),
                ('visibility', models.CharField(choices=[('Me', 'Only Me'), ('All', 'All'), ('INC', 'Incubator'), ('SU', 'Start ups'), ('SUT', 'Start Up Team'), ('INCT', 'Incubator Team')], max_length=10, verbose_name='Contact Visibility')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': ['user'],
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Incubator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('website', models.URLField(blank=True, null=True)),
                ('short_description', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('request_designation', models.CharField(max_length=200)),
                ('space_info', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[('A', 'Approved'), ('P', 'In Progress'), ('R', 'Rejected'), ('S', 'Submitted')], default='S', max_length=10)),
                ('followers', models.ManyToManyField(related_name='incubator_follows', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IncubatorAchievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(blank=True)),
                ('title', models.CharField(max_length=255)),
                ('incubator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievements', to='app.Incubator')),
            ],
            options={
                'ordering': ['incubator'],
                'verbose_name_plural': 'Achievements - Startup',
            },
        ),
        migrations.CreateModel(
            name='IncubatorContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.CharField(choices=[('Mob', 'Mobile No.'), ('Email', 'Email')], max_length=10, verbose_name='Contact Type')),
                ('value', models.TextField()),
                ('visibility', models.CharField(choices=[('Me', 'Only Me'), ('All', 'All'), ('INC', 'Incubator'), ('SU', 'Start ups'), ('SUT', 'Start Up Team'), ('INCT', 'Incubator Team')], default='All', max_length=10, verbose_name='Contact Visibility')),
                ('incubator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='app.Incubator')),
            ],
            options={
                'ordering': ['incubator'],
                'verbose_name_plural': 'Incubator Contacts',
            },
        ),
        migrations.CreateModel(
            name='IncubatorFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('file_added', models.FileField(upload_to='media/incubators/docs')),
                ('incubator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Incubator')),
            ],
        ),
        migrations.CreateModel(
            name='IncubatorImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('file_added', models.ImageField(upload_to='media/incubators/imgs')),
                ('incubator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Incubator')),
            ],
        ),
        migrations.CreateModel(
            name='IncubatorMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_level', models.CharField(choices=[('A', 'Admin'), ('M', 'Member')], default='M', max_length=10)),
                ('role', models.CharField(max_length=100)),
                ('joining_date', models.DateTimeField(auto_now_add=True)),
                ('incubator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Incubator')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IncubatorPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(blank=True)),
                ('title', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='media/incubators/posts')),
                ('post_type', models.CharField(choices=[('P', 'Post'), ('C', 'Competition')], max_length=10, verbose_name='Contact Visibility')),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('incubator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='app.Incubator')),
            ],
            options={
                'ordering': ['incubator'],
                'verbose_name_plural': 'Posts - Incubator',
            },
        ),
        migrations.CreateModel(
            name='IncubatorSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_type', models.CharField(choices=[('FB', 'Facebook'), ('TW', 'Twitter'), ('IN', 'Instagram'), ('SC', 'Snap Chat'), ('LI', 'Linked In'), ('GH', 'Github')], max_length=10, verbose_name='Contact Type')),
                ('value', models.URLField()),
                ('visibility', models.CharField(choices=[('Me', 'Only Me'), ('All', 'All'), ('INC', 'Incubator'), ('SU', 'Start ups'), ('SUT', 'Start Up Team'), ('INCT', 'Incubator Team')], default='All', max_length=10, verbose_name='Social Visibility')),
                ('incubator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socials', to='app.Incubator')),
            ],
            options={
                'verbose_name_plural': 'Social Accounts - Incubator',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latlong', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('deleted', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('links', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Link')),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_type', models.CharField(choices=[('UN', 'University'), ('CG', 'Campus Group'), ('C', 'Company')], max_length=10, verbose_name='Organisation Type')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('url', models.URLField(blank=True, null=True)),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=20, unique=True)),
                ('links', models.ManyToManyField(through='app.Link', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('users', models.ManyToManyField(blank=True, related_name='skills', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_type', models.CharField(choices=[('FB', 'Facebook'), ('TW', 'Twitter'), ('IN', 'Instagram'), ('SC', 'Snap Chat'), ('LI', 'Linked In'), ('GH', 'Github')], max_length=10, verbose_name='Contact Type')),
                ('value', models.URLField()),
                ('visibility', models.CharField(choices=[('Me', 'Only Me'), ('All', 'All'), ('INC', 'Incubator'), ('SU', 'Start ups'), ('SUT', 'Start Up Team'), ('INCT', 'Incubator Team')], max_length=10, verbose_name='Social Visibility')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socials', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Social Accounts',
            },
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('website', models.URLField(blank=True, null=True)),
                ('short_description', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('request_designation', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[('A', 'Approved'), ('P', 'In Progress'), ('R', 'Rejected'), ('S', 'Submitted')], default='S', max_length=10)),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Location')),
            ],
        ),
        migrations.CreateModel(
            name='StartupAchievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(blank=True)),
                ('title', models.CharField(max_length=255)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievements', to='app.Startup')),
            ],
            options={
                'ordering': ['startup'],
                'verbose_name_plural': 'Achievements - Startup',
            },
        ),
        migrations.CreateModel(
            name='StartupContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.CharField(choices=[('Mob', 'Mobile No.'), ('Email', 'Email')], max_length=10, verbose_name='Contact Type')),
                ('value', models.TextField()),
                ('visibility', models.CharField(choices=[('Me', 'Only Me'), ('All', 'All'), ('INC', 'Incubator'), ('SU', 'Start ups'), ('SUT', 'Start Up Team'), ('INCT', 'Incubator Team')], default='All', max_length=10, verbose_name='Contact Visibility')),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='app.Startup')),
            ],
            options={
                'ordering': ['startup'],
                'verbose_name_plural': 'Contacts - Startup',
            },
        ),
        migrations.CreateModel(
            name='StartupFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('file_added', models.FileField(upload_to='media/startups/docs')),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Startup')),
            ],
        ),
        migrations.CreateModel(
            name='StartupMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_level', models.CharField(choices=[('A', 'Admin'), ('M', 'Member')], default='M', max_length=10)),
                ('role', models.CharField(max_length=100)),
                ('joining_date', models.DateTimeField(auto_now_add=True)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Startup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StartupsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('file_added', models.ImageField(upload_to='media/startups/imgs')),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Startup')),
            ],
        ),
        migrations.CreateModel(
            name='StartupSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_type', models.CharField(choices=[('FB', 'Facebook'), ('TW', 'Twitter'), ('IN', 'Instagram'), ('SC', 'Snap Chat'), ('LI', 'Linked In'), ('GH', 'Github')], max_length=10, verbose_name='Contact Type')),
                ('value', models.URLField()),
                ('visibility', models.CharField(choices=[('Me', 'Only Me'), ('All', 'All'), ('INC', 'Incubator'), ('SU', 'Start ups'), ('SUT', 'Start Up Team'), ('INCT', 'Incubator Team')], default='All', max_length=10, verbose_name='Social Visibility')),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socials', to='app.Startup')),
            ],
            options={
                'verbose_name_plural': 'Social Accounts - Startup',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('followers', models.ManyToManyField(blank=True, related_name='tags', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date Of Birth')),
                ('gender', models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male')], max_length=1, null=True, verbose_name='gender')),
                ('aadhar_no', models.BigIntegerField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, default='Indian', max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='startup',
            name='members',
            field=models.ManyToManyField(related_name='startup_members', through='app.StartupMember', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='startup',
            name='request_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='startup_request', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='startup',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='startups', to='app.Tag'),
        ),
        migrations.AddField(
            model_name='startup',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='startup', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='link',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Room'),
        ),
        migrations.AddField(
            model_name='link',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='incubator',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Location'),
        ),
        migrations.AddField(
            model_name='incubator',
            name='members',
            field=models.ManyToManyField(related_name='incubator_members', through='app.IncubatorMember', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='incubator',
            name='request_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='incubator_request', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='incubator',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='incubators', to='app.Tag'),
        ),
        migrations.AddField(
            model_name='incubator',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='incubator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='experience',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='app.Organisation'),
        ),
        migrations.AddField(
            model_name='experience',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to=settings.AUTH_USER_MODEL),
        ),
    ]
