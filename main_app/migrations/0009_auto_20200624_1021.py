# Generated by Django 3.0.5 on 2020-06-24 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20200623_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='thread',
        ),
        migrations.AddField(
            model_name='message',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.Post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=500),
        ),
        migrations.DeleteModel(
            name='Thread',
        ),
    ]
