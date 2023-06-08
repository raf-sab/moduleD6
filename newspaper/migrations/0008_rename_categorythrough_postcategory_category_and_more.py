# Generated by Django 4.1.7 on 2023-03-30 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0007_category_subscribers_alter_post_categorytype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcategory',
            old_name='categoryThrough',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='postcategory',
            old_name='postThrough',
            new_name='post',
        ),
        migrations.AlterField(
            model_name='post',
            name='postCategory',
            field=models.ManyToManyField(blank=True, through='newspaper.PostCategory', to='newspaper.category'),
        ),
    ]