from django.db import models


class Post(models.Model):
    imgurl = models.CharField(max_length=128,
                                verbose_name='이미지 주소')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('dsuser.Dsuser', on_delete=models.CASCADE,
    verbose_name='작성자')
    tags = models.ManyToManyField('tag.Tag', verbose_name='태그')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                            verbose_name='작성일')
    
    def __str__(self):
        return self.writer

    class Meta:
        db_table = 'djangostagram_post'
        verbose_name = 'DJANGOSTAGRAM 게시글'
        verbose_name_plural = 'DJANGOSTAGRAM 게시글'