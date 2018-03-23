# Generated by Django 2.0.3 on 2018-03-23 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animation_type', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=200)),
                ('font', models.CharField(max_length=200)),
                ('font_size', models.IntegerField(default=11)),
                ('pos_top', models.IntegerField(default=100)),
                ('pos_left', models.IntegerField(default=50)),
                ('time_app', models.IntegerField(default=10)),
                ('time_dis', models.IntegerField(default=10)),
                ('size_w', models.CharField(max_length=5)),
                ('size_h', models.CharField(max_length=5)),
                ('path', models.CharField(max_length=200)),
                ('is_image', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='animation',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Video'),
        ),
    ]
