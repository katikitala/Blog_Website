# Generated by Django 3.2.7 on 2021-10-06 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('New_blog', '0006_post_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='Description',
        ),
    ]