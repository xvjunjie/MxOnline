from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here
class UserProfile(AbstractUser):
    '''用户信息'''
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )

    nice_name = models.CharField(max_length=30, default='', verbose_name=u'昵称')
    birthday = models.DateField(blank=True, null=True, verbose_name=u'生日')
    gender = models.BooleanField(choices=GENDER_CHOICES, default='male')
    address = models.CharField(max_length=100, default='', verbose_name=u'地址')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'手机')
    AvatarImg = models.ImageField(upload_to='images/%Y/%m', max_length=100, default='', verbose_name=u'头像')

    class Meta:
        ''' meta信息，即后台栏目名'''
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username



class EmailVerifyRecord(models.Model):
    '''邮箱验证码'''
    SEND_CHOICES = (
        ("register", u"注册"),
        ("forget", u"找回密码")
    )


    code = models.CharField(max_length=10,verbose_name=u'验证码')
    email = models.EmailField(max_length=50,verbose_name=u'邮箱')
    send_type = models.CharField(max_length=10,choices=SEND_CHOICES,verbose_name=u'发送类型')
    #这里的now得去掉(), 不去掉会根据编译时间。而不是根据实例化时间
    send_time = models.DateTimeField(default=datetime.now)


    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name




class PageBanner(models.Model):
    '''轮播图
        1.图片 2. 点击图片地址 3. 轮播图序号(控制前后)
    '''
    title = models.CharField(max_length=100,verbose_name=u'标题')
    ulr = models.URLField(max_length=200,verbose_name=u'访问链接')
    image = models.ImageField(max_length=100,upload_to='banner/%Y/%m',verbose_name=u'轮播图')
    #越大越靠后
    index = models.IntegerField(default=1,verbose_name=u'图片前后位置')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name

