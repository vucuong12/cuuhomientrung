# Generated by Django 3.1.2 on 2020-10-19 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_auto_20201019_0449'),
    ]

    operations = [
        migrations.CreateModel(
            name='NguonLuc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='', verbose_name='Nguồn lực')),
                ('location', models.TextField(blank=True, default='', verbose_name='Địa chỉ')),
                ('status', models.IntegerField(choices=[(1, 'Sẵn sàng'), (2, 'Không gọi được'), (3, 'Đang nghỉ/Hết tài nguyên')], default=0, verbose_name='Tình trạng')),
                ('phone', models.TextField(blank=True, default='', verbose_name='Điện thoại liên hệ')),
                ('note', models.TextField(blank=True, default='', verbose_name='Ghi chú')),
                ('huyen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.huyen')),
                ('thon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.thon')),
                ('tinh', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.tinh')),
                ('volunteer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.tinhnguyenvien', verbose_name='Tình nguyện viên xác minh')),
                ('xa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.xa')),
            ],
        ),
    ]
