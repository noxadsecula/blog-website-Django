# Generated by Django 4.1.3 on 2023-02-17 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_comment_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-commentDate']},
        ),
    ]
