# Generated by Django 3.2.10 on 2022-01-05 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20220103_1307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['parent__id', 'position'], 'verbose_name': 'دسته\u200cبندی', 'verbose_name_plural': 'دسته\u200cبندی\u200cها'},
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده'),
        ),
    ]
