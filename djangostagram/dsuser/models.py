from django.db import models


class Dsuser(models.Model):
    userid = models.CharField(max_length=32,
                                verbose_name='아이디')
    email = models.EmailField(max_length=128,
                                verbose_name='사용자이메일')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                            verbose_name='가입일')
    

    
    def __str__(self):
        return self.userid

    class Meta:
        db_table = 'djangostagram_dsuser'
        verbose_name = 'DJANGOSTAGRAM 사용자'
        verbose_name_plural = 'DJANGOSTAGRAM 사용자'