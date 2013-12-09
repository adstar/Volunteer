# coding=utf-8
from django.db import models
from django.contrib.auth.models import User, Group

# 机构表
class Institution(models.Model):
    # 机构ID： 3XX
    inst_id = models.CharField(max_length=20, primary_key=True, unique=True)
    inst_name = models.CharField(max_length=40, unique=True)

    def __unicode__(self):
        return self.inst_name

# 志愿者基本信息表
class CommonUser(models.Model):
    # admin.auth.User 学号 姓名 邮箱 密码（SHA）
    user = models.OneToOneField(User)
    # 用户联系电话
    cu_tel = models.CharField(max_length=11)
    # 用户未加密密码
    password1 = models.CharField(max_length=25)
    # 用户头像
    user_pic = models.ImageField(upload_to='userImg/%Y/%m/%d')
    # 志愿者总志愿时间，最大不超过999小时，保留两位小数
    cu_actTime = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    # 用户所在学院
    inst = models.ForeignKey(Institution)

#    def __unicode__(self):
#        return self.user

# 管理用户表
class ManageUser(models.Model):
    # admin.auth.User 管理用户ID 管理用户名称 密码（SHA）
    mu_user = models.OneToOneField(User)
    # 管理用户密码
    mu_pass1 = models.CharField(max_length=10)
    # 管理用户总时间 不超过9999小时，保留两位小数
    mu_time = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    # 管理用户介绍
    mu_desc = models.TextField()
    # 管理用户所属机构
    inst = models.ForeignKey(Institution)
    # 管理用户所属组别
    group = models.ForeignKey(Group)

    def __unicode__(self):
        return self.mu_name

    # 返回服务队的简称 如 “朝阳”青年志愿者服务队
    def shortName(self):
        print self.mu_name.find('“')
        return self.mu_name[self.mu_name.find('“'):]

# 活动基本信息表
class ActivityInfo(models.Model):
    # 活动状态
    UC = 'UC'  # 活动未审核 UnChecked
    CU = 'CU'  # 活动已审核通过，未完成  CheckedUndone
    RE = 'RE'  # 活动审核未通过  REjected
    CD = 'CD'  # 活动已完成  CheckedDone
    CHECK_CHOICE = (
        (UC, '待审核'),
        (CU, '审核通过'),
        (RE, '审核未通过'),
        (CD, '活动完成'),
    )
    # 活动类型
    ED = 'ED' # 校园教辅
    LF = 'LF' # 校园生活
    CM = 'CM' # 社区建设
    YU = 'YU' # 关爱青少年
    OD = 'OD' # 扶老助残
    HL = 'HL' # 救防保健
    GM = 'GM' # 大型赛会
    SP = 'SP' # 特色服务
    OT = 'OT' # 其他
    CATEGORY_CHOICE = (
        (ED, '校园教辅'),
        (LF, '校园生活'),
        (CM, '社区建设'),
        (YU, '关爱青少年'),
        (OD, '扶老助残'),
        (HL, '救防保健'),
        (GM, '大型赛会'),
        (SP, '特色服务'),
        (OT, '其他')
    )
    # 活动ID： 3（活动提交时间YY-MM-DD-hh-mm + 活动主办方4XX + 2为序数XX） HASH
    act_id = models.CharField(max_length=15, primary_key=True, unique=True)
    # 活动时长
    act_interval = models.PositiveIntegerField()
    # 活动举办时间
    act_time = models.DateTimeField()
    # 活动地点
    act_place = models.CharField(max_length=45)
    # 活动标题
    act_title = models.CharField(max_length=45)
    # 活动类别
    act_category = models.CharField(max_length=2, choices=CATEGORY_CHOICE, default='ED')
    # 活动介绍
    act_desc = models.TextField()
    # 活动提交时间
    act_postTime = models.DateTimeField(auto_now_add=True, editable=False)
    # 活动是否通过审核
    act_check = models.CharField(max_length=2, choices=CHECK_CHOICE, default='UC')
    # 报名截止日期
    act_deadline = models.DateTimeField()
    # 活动预设报名人数
    act_number = models.PositiveIntegerField(default=20)
    # 活动策划
    act_plan = models.FileField(upload_to='plan/%Y/%m/%d')
    # 活动照片
    act_picture = models.ImageField(upload_to='actImg/%Y/%m/%d')
    # 活动主办方（服务队）
    team_id = models.ForeignKey(ManageUser)

    def __unicode__(self):
        return self.act_title

# 活动新闻表
class ActivityNews(models.Model):
    # 活动新闻ID 6（{活动ID}XXXXXXXXXXXX）（{一位随机数}X）
    news_id = models.CharField(max_length=15, primary_key=True, unique=True)
    # 活动新闻标题
    news_title = models.CharField(max_length=45)
    # 活动新闻内容
    news_body = models.TextField()
    # 活动新闻提交时间
    news_time = models.DateTimeField(auto_now_add=True, editable=False)
    # 新闻浏览次数
    news_count = models.PositiveIntegerField(default=1)
    # 新闻照片
    news_picture = models.ImageField(upload_to='newsImg/%Y/%m/%d')
    # 活动ID
    act = models.ForeignKey(ActivityInfo)

    def __unicode__(self):
        return self.news_title


# 活动评论表
class ActivityComment(models.Model):
    # 活动评论ID：9（{发表时间YYYY-MM-DD-hh-mm}XXXXXXXXXXXX）（{评论者ID}）（{主办方ID}）
    actCom_id = models.CharField(max_length=15, primary_key=True, unique=True)
    # 活动评论内容
    actCom_content = models.TextField()
    # 活动评论发表时间
    actCom_time = models.DateTimeField(auto_now_add=True, editable=False)
    # 活动评论发表者ID
    sno = models.ForeignKey(CommonUser)
    # 活动ID
    act = models.ForeignKey(ActivityInfo)

    def __unicode__(self):
        return self.actCom_id

# 活动报名表
class ActivityRegister(models.Model):
    # 报名审核状态
    UC = 'UnChecked'
    CU = 'CheckedUndone'
    RE = 'Rejected'
    CD = 'CheckedDone'
    CHECK_CHOICE = (
        (UC, '待审核'),
        (CU, '审核通过'),
        (RE, '审核未通过'),
        (CD, '活动完成'),
    )
    # 活动报名ID
    actRegist_id = models.CharField(max_length=15, primary_key=True, unique=True)
    # 活动报名时间
    actRegist_time = models.DateTimeField(auto_now_add=True, editable=False)
    # 活动报名是否成功
    actRegist_check = models.CharField(max_length=2, choices=CHECK_CHOICE, default=UC)
    # 活动报名用户ID
    sno_id = models.ForeignKey(CommonUser)
    # 活动ID
    act_id = models.ForeignKey(ActivityInfo)

    def __unicode__(self):
        return self.actRegist_id

# 活动总结表
class ActivitySummary(models.Model):
    # 活动总结ID
    actSummary_id = models.CharField(max_length=15, primary_key=True, unique=True)
    # 活动总结内容
    actSummary_file = models.FileField(upload_to='summary/%Y/%m/%d')
    # 活动总结提交时间
    actSummary_time = models.DateTimeField(auto_now_add=True, editable=False)
    # 活动ID
    act_id = models.ForeignKey(ActivityInfo)

    def __unicode__(self):
        return self.actSummary_id

# 上传的文件
# class PostedFile(models.Model):
#     # 文件标题
#     file_title = models.CharField()
