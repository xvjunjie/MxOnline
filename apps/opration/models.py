from datetime import datetime
from django.db import models

# Create your models here.
from courses.models import Course
from users.models import UserProfile


class UserAsk(models.Model):
    '''
        用户我要学习表单
    '''
    name = models.CharField(max_length=20, verbose_name=u"姓名")
    mobile = models.CharField(max_length=11, verbose_name=u"手机")
    course_name = models.CharField(max_length=50, verbose_name=u"课程名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    '''
        用户对于课程评论
        那个用户对那个课程做出评价
    '''
    course = models.ForeignKey(Course, verbose_name=u"课程",on_delete=models.Case)
    user = models.ForeignKey(UserProfile, verbose_name=u"用户",on_delete=models.Case)
    comments = models.CharField(max_length=250, verbose_name=u"评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"评论时间")

    class Meta:
        verbose_name = u"课程评论"
        verbose_name_plural = verbose_name





class UserFavorite(models.Model):
    '''
        用户对于课程,机构，讲师的收藏
        那个用户对，机构，课程，还是老师；做了收藏
    '''


    TYPE_CHOICES = (
        (1, u"课程"),
        (2, u"课程机构"),
        (3, u"讲师")
    )

    user = models.ForeignKey(UserProfile, verbose_name=u"用户",on_delete=models.Case)
    # course = models.ForeignKey(Course, verbose_name=u"课程")
    # teacher = models.ForeignKey()
    # org = models.ForeignKey()
    # fav_type =

    # 机智版
    # 直接保存用户的id.
    fav_id = models.IntegerField(default=0)
    # 表明收藏的是哪种类型。
    fav_type = models.IntegerField(
        choices=TYPE_CHOICES,
        default=1,
        verbose_name=u"收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"评论时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name





class UserMessage(models.Model):
    '''
        用户消息表
        因为我们的消息有两种:发给全员和发给某一个用户。
        所以如果使用外键，每个消息会对应要有用户。很难实现全员消息。
    '''


    # 机智版 为0发给所有用户，不为0就是发给用户的id
    user = models.IntegerField(default=0, verbose_name=u"接收用户")
    message = models.CharField(max_length=500, verbose_name=u"消息内容")

    # 是否已读: 布尔类型 BooleanField False未读,True表示已读
    has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name



class UserCourse(models.Model):
    '''
        用户课程表
        哪个用户学习了哪门课程
    '''
    course = models.ForeignKey(Course, verbose_name=u"课程",on_delete=models.Case)
    user = models.ForeignKey(UserProfile, verbose_name=u"用户",on_delete=models.Case)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name