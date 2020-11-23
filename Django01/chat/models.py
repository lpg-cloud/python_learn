import channels
from django.db import models
from django.db.models.base import Model


# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=20)

#用来存储用户登录时和服务器建立的连接的channels_name
class client(models.Model):
    channel_name = models.CharField(max_length=40)
    user_name = models.OneToOneField(to=user, on_delete=models.CASCADE)
    login_time = models.DateTimeField('date_login')
    
class group(models.Model):
    name = models.CharField(max_length=20)
    icon = models.URLField()
    profile = models.CharField(max_length=200, verbose_name='简介',default='')

#用户对群的消息提醒设置选项
message_set_choise=(
    (1,'接收并提醒'),
    (2,'接收但不提醒'),
    (3,'接收但不提醒'),
    (4,'屏蔽群消息'),
)

#用户群组关系表
class userGroupRelation(models.Model):
    user_id = models.ForeignKey(user, on_delete=models.CASCADE, related_name='group_set')
    group_id = models.ForeignKey(group, on_delete=models.CASCADE, related_name='user_set')
    nick_name = models.CharField(max_length=20)
    message_set = models.BigIntegerField(choices=message_set_choise, default=1)
    is_admin = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    chat_background_img = models.URLField()

#消息类型
message_type = (
    (1,'text'),
    (2,'files'),
)

#会话列表，qq第一页
class chat(models.Model):
    start_time = models.DateTimeField(verbose_name="会话开始时间", auto_now=False, auto_now_add=False)
    owner = models.ForeignKey(user, verbose_name='所属用户', on_delete= models.CASCADE, related_name='charts_set' ,null=False)

#用户发送给用户的消息
class userMessage(models.Model):
    sender = models.ForeignKey(user, on_delete=models.CASCADE, related_name='sended_messages')
    datetime_send = models.DateTimeField(auto_now_add=True)
    receiver = models.ForeignKey(user, on_delete=models.CASCADE, related_name='received_user_messages')
    content_type = models.BigIntegerField(choices=message_type)
    content = models.CharField(max_length=200)
    chat_id = models.ManyToManyField(chat, verbose_name="接收到的用户信息", related_name='user_messages')

#用户发送到群中的消息
class groupMessage(models.Model):
    sender = models.ForeignKey(user, verbose_name="发送人", on_delete=models.CASCADE)
    group_id = models.ForeignKey(group, verbose_name="接收的群", on_delete=models.CASCADE, related_name='groupMessage_set')
    datetime_send = models.DateTimeField(auto_now_add=True)
    content_type = models.BigIntegerField(choices=message_type)
    content = models.CharField(max_length=200)
    chat_id = models.ManyToManyField(chat, verbose_name="接收到的群组信息", related_name='group_messages')

