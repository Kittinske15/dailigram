# Generated by Django 2.1.1 on 2018-11-10 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story', models.TextField(help_text='Write your story.', max_length=100000)),
                ('date', models.DateField(verbose_name='Date')),
                ('picture', models.FileField(upload_to='')),
                ('diary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diary.Diary')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a tag (e.g. Love, Happy, Sad)', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diary.Tag'),
        ),
    ]
