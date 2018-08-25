from django.db import models
from datetime import datetime


# Create your models here.

class Course(models.Model):
    '''课程信息'''

    DEGREE_CHOICES = (
        ("cj", u"初级"),
        ("zj", u"中级"),
        ("gj", u"高级")
    )

    name = models.CharField(max_length=50, verbose_name=u'标题')
    desc = models.CharField(max_length=200, verbose_name=u'描述')
    # TextField允许我们不输入长度。可以输入到无限大。暂时定义为TextFiled，之后更新为富文本
    detail = models.TextField(verbose_name=u'详情')
    degree = models.CharField(max_length=2, choices=DEGREE_CHOICES, verbose_name=u'难度等级')
    learn_time = models.IntegerField(default=0, verbose_name=u'学习时长')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏数')
    image = models.ImageField(max_length=100, upload_to='courses/%Y/%m', verbose_name=u'封面图')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程信息'
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    '''章节
        因为一个课程对应很多章节。所以在章节表中将课程设置为外键。
        作为一个字段来让我们可以知道这个章节对应那个课程
    '''

    course = models.ForeignKey(Course, on_delete=models.Case, verbose_name=u'课程')
    name = models.CharField(max_length=50, verbose_name=u'章节标题')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name


class Video(models.Model):
    '''
        每章节视频
        因为一个章节对应很多视频。所以在视频表中将章节设置为外键。
        作为一个字段来存储让我们可以知道这个视频对应哪个章节.

    '''

    lesson = models.ForeignKey(Lesson, verbose_name=u'章节',on_delete=models.Case)
    name = models.CharField(max_length=50, verbose_name=u'视频名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name
        verbose_name_plural = verbose_name


# 课程资源
class CourseResource(models.Model):
    '''
        课程资源
        因为一个课程对应很多资源。所以在课程资源表中将课程设置为外键。
        作为一个字段来让我们可以知道这个资源对应那个课程
    '''

    course = models.ForeignKey(Course, verbose_name=u"课程",on_delete=models.Case)
    name = models.CharField(max_length=100, verbose_name=u"名称")
    # 这里定义成文件类型的field，后台管理系统中会直接有上传的按钮。
    # FileField也是一个字符串类型，要指定最大长度。
    download = models.FileField(
        upload_to="course/resource/%Y/%m",
        verbose_name=u"资源文件",
        max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name
