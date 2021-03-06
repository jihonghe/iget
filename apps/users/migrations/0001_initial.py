# Generated by Django 2.1.7 on 2019-05-10 21:00

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否激活')),
                ('nickname', models.CharField(blank=True, max_length=20, null=True, verbose_name='昵称')),
                ('head_img', models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='头像')),
                ('gender', models.IntegerField(choices=[(0, '男'), (1, '女')], default=0, verbose_name='性别')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户账号',
                'verbose_name_plural': '用户账号',
                'ordering': ['create_time'],
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='EmailVerification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_email', models.EmailField(max_length=100, verbose_name='目标邮箱')),
                ('verify_type', models.IntegerField(choices=[(0, 'activate'), (1, 'reset_pwd'), (2, 'ch_pwd'), (3, 'che_email')], verbose_name='验证类型')),
                ('code', models.CharField(max_length=254, verbose_name='邮箱验证码')),
                ('send_time', models.DateTimeField(auto_now_add=True, verbose_name='发送时间')),
                ('is_valid', models.BooleanField(default=True, verbose_name='验证码是否有效')),
            ],
            options={
                'verbose_name': '邮箱验证码',
                'verbose_name_plural': '邮箱验证码',
                'ordering': ['send_time'],
            },
        ),
        migrations.CreateModel(
            name='MailWebSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_site', models.CharField(max_length=100, verbose_name='邮箱登录链接')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='消息标题')),
                ('content', models.TextField(verbose_name='消息内容')),
                ('send_type', models.IntegerField(choices=[(0, '公共消息'), (1, '个人消息')], default=0, verbose_name='消息发送类型')),
                ('send_time', models.DateField(auto_now_add=True, verbose_name='消息发送时间')),
                ('end_time', models.DateField(verbose_name='消息有效性截止时间')),
            ],
            options={
                'verbose_name': '消息阅读日志',
                'verbose_name_plural': '消息阅读日志',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='MessageReadLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='消息接收者id')),
                ('msg_id', models.IntegerField(verbose_name='消息id')),
                ('status', models.IntegerField(choices=[(-1, '删除'), (0, '未读'), (1, '已读')], default=0, verbose_name='消息状态')),
            ],
            options={
                'verbose_name': '消息阅读日志',
                'verbose_name_plural': '消息阅读日志',
                'ordering': ['user_id'],
            },
        ),
    ]
