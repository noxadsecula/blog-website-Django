# Generated by Django 4.1.3 on 2023-02-08 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_articleimage_alter_article_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentAuthor', models.CharField(max_length=20, verbose_name='Author')),
                ('commentContent', models.CharField(max_length=200, verbose_name='Comment')),
                ('commentDate', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comments', to='article.article', verbose_name='Article')),
            ],
        ),
    ]
