# Generated by Django 4.0.2 on 2022-02-18 21:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_book_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='details',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]