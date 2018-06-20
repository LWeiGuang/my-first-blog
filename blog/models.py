from django.db import models
from django.utils import timezone
# Create your models here.

# 定义博客模型
class Post(models.Model):
    # 文章作者
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # 标题，短文本
    title = models.CharField(max_length=200)
    # 内容，长文本内容
    text = models.TextField()
    # 文章创建时间
    careated_date = models.DateTimeField(default=timezone.now)

    published_date = models.DateTimeField(blank=True, null=True)

    # 博客文章发布方法
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # 返回文章标题
    def __str__(self):
        return self.title
