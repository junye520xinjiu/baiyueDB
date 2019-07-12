from django.db import models

# Create your models here.


class Md_link(models.Model):

    magnetic_link = models.CharField(max_length=150,null=True,verbose_name='磁力下载连接')

    def __str__(self):
        return '磁力下载连接:%s'%self.magnetic_link

    class Meta:
        db_table = 'Md_link'
        verbose_name = '磁力下载链接表'
        verbose_name_plural = '磁力下载链接表'


class Movie(models.Model):

    movie_name = models.CharField(max_length=100,null=True,db_index=True,verbose_name='电影名称')
    release_time = models.CharField(max_length=100,null=True,db_index=True,verbose_name='上映时间')
    file_size = models.CharField(max_length=100,null=True,db_index=True,verbose_name='文件大小')
    act_role = models.CharField(max_length=400,null=True,db_index=True,verbose_name='主演')
    md_link = models.ForeignKey(Md_link,on_delete=models.CASCADE)

    def __str__(self):
        return '电影名称:%s,上映时间:%s,豆瓣评分:%s,主演:%s'%(self.movie_name,self.release_time,self.file_size,self.act_role)

    class Meta:
        db_table = 'Movie'
        verbose_name = '电影表'
        verbose_name_plural = '电影信息'


