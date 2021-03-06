# Generated by Django 3.1.2 on 2020-10-19 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_hodan_need'),
    ]

    operations = [
        migrations.CreateModel(
            name='TinTuc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, default='', verbose_name='Tin')),
                ('url', models.TextField(blank=True, default='', verbose_name='Link')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Cập nhật')),
                ('note', models.TextField(blank=True, default='', verbose_name='Ghi chú')),
            ],
            options={
                'verbose_name': 'Nguồn trợ giúp khác',
                'verbose_name_plural': 'c',
            },
        ),
        migrations.AlterModelOptions(
            name='nguonluc',
            options={'verbose_name': 'Nguồn trợ giúp khác', 'verbose_name_plural': 'Nguồn trợ giúp khác'},
        ),
        migrations.AddField(
            model_name='cuuho',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Cập nhật'),
        ),
        migrations.AddField(
            model_name='hodan',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Cập nhật'),
        ),
        migrations.AddField(
            model_name='nguonluc',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Cập nhật'),
        ),
    ]
