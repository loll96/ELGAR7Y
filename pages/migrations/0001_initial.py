# Generated by Django 3.1.4 on 2021-02-08 00:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=20)),
                ('subjct', models.CharField(max_length=100)),
                ('whatq', models.CharField(choices=[('اقتصادي', 'اقتصادي'), ('سياسي', 'سياسي'), ('رياضي', 'رياضي'), ('تواصل', 'تواصل')], max_length=100)),
                ('what', models.CharField(choices=[('استثمارات', 'استثمارات'), ('انشاءات', 'انشاءات'), ('تنمية وتطوير', 'تنمية وتطوير'), ('غير ذلك', 'غير ذلك')], max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RewardsCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Say',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/say')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('job', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('link', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SrCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/sr')),
                ('content', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.srcategories')),
                ('sources', models.ManyToManyField(to='pages.Source')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/News')),
                ('title', models.CharField(max_length=200)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('content', models.TextField()),
                ('bigcontent', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.newscategories')),
                ('sources', models.ManyToManyField(to='pages.Source')),
            ],
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/awards')),
                ('title', models.CharField(max_length=100)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('content', models.TextField()),
                ('bigcontent', models.TextField()),
                ('df', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.rewardscategories')),
                ('sources', models.ManyToManyField(to='pages.Source')),
            ],
        ),
    ]
