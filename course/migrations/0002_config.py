# Generated by Django 2.1 on 2018-11-12 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('template', models.CharField(choices=[('bootstrap', 'bootstrap'), ('bootswatch', 'bootswatch')], max_length=20, verbose_name='模板')),
                ('theme', models.CharField(choices=[('bootstrap', 'bootstrap'), ('bootswatch', 'bootswatch')], max_length=20, verbose_name='模板')),
                ('gen_static_pages', models.BooleanField(default=False, verbose_name='是否生成静态页面')),
            ],
            options={
                'verbose_name': '配置',
                'verbose_name_plural': '配置',
            },
        ),
    ]