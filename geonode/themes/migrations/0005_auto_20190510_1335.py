# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-10 13:35


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geonode_themes', '0004_auto_20190503_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='geonodethemecustomization',
            name='navbar_dropdown_menu',
            field=models.CharField(default=b'#2c689c', max_length=10),
        ),
        migrations.AddField(
            model_name='geonodethemecustomization',
            name='navbar_dropdown_menu_divider',
            field=models.CharField(default=b'#204d74', max_length=10),
        ),
        migrations.AddField(
            model_name='geonodethemecustomization',
            name='navbar_dropdown_menu_hover',
            field=models.CharField(default=b'#204d74', max_length=10),
        ),
        migrations.AddField(
            model_name='geonodethemecustomization',
            name='navbar_dropdown_menu_text',
            field=models.CharField(default=b'#ffffff', max_length=10),
        ),
        migrations.AddField(
            model_name='geonodethemecustomization',
            name='navbar_text_color',
            field=models.CharField(default=b'#ffffff', max_length=10),
        ),
        migrations.AddField(
            model_name='geonodethemecustomization',
            name='navbar_text_hover',
            field=models.CharField(default=b'#2c689c', max_length=10),
        ),
        migrations.AddField(
            model_name='geonodethemecustomization',
            name='navbar_text_hover_focus',
            field=models.CharField(default=b'#2c689c', max_length=10),
        ),
    ]
