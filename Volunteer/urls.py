# coding=utf-8
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # 首页
    url(r'^$', 'users.views.home', name='home'),
    url(r'^home/$', 'users.views.home', name='home'),
    url(r'^index/$', 'users.views.home', name='home'),
    
    # 用户登陆
    url(r'^login/$', 'users.views.loginInit', name='login'),
    url(r'^login/handler/$', 'users.views.loginHandler', name='loginHandler'),
    # 用户登出
    url(r'^logout/$', 'users.views.logoutInit', name='logout'),
    url(r'^logout/handler/$', 'users.views.logoutHandler', name='logoutHandler'),
    # 普通用户注册
    url(r'^register/$', 'users.views.registerInit', name='register'),
    url(r'^register/handler/$', 'users.views.registerHandler', name='registerHandler'),

    # 重置密码
    url(r'^resetpassword$','users.views.resetPasswordInit', name='resetPassword'),
    url(r'^forgetpassword/handler/$', 'users.views.resetPasswordHandler', name='resetPasswordHandler'),

    # 志愿者个人主页
    url(r'^user/\d+/$', 'users.views.userPage', name='userPage'),
    # 志愿者参加过的活动列表
    url(r'^user/\d+/activity$', 'users.views.userActivityList', name='userActivityList'),
    # 志愿者的留言列表
    url(r'^user/\d+/message$', 'users.views.userMessageList',  name='userMessageList'),
    # 志愿者的广播列表
      url(r'^user/\d+/broadcast$', 'users.views.userBroadcastList',  name='userBroadcastList'),
    # 志愿者更改个人信息页
    url(r'^user/\d+/infochange$', 'users.views.userInfoChange', name='userInfoChange'),

    # 全部活动列表
    url(r'^activity_all/$', 'activity.views.activityList', name='activityList'),
    # 活动详情页
    url(r'^activity/\d+$', 'activity.views.activityDetail', name='activityDetail'),
    # 活动全部成员
    url(r'^activity/\d+/member$', 'activity.views.activityMember', name='activityMember'),
    # 活动全部评价
    url(r'^activity/\d+/message$', 'activity.views.activityComment', name='activityComment'),

    # 活动组织方首页
    url(r'^manager/\d+/home$', 'manager.views.home', name='managerHome'),
    # 活动组织方信息展示页
     url(r'^manager/\d+$', 'manager.views.managerInfo', name='managerPage'),
    # 组织方活动列表页
     url(r'^manager/\d+activity_all$', 'manager.views.managerActivityList', name='managerActivityList'),
    # 筛选志愿者
    url(r'^manager/act/\d+/check$', 'manager.views.checkVolunteer', name='checkVolunteer'),
    # 更新志愿者时间
    url(r'^manager/act/\d+/changetime', 'manager.views.timeUpdate', name='timeUpdate'),
    # 申请活动
    url(r'^manager/\d+/post$', 'manager.views.activityPost', name='activityPost'),
    # 发布新闻
     url(r'^manager/\d+/newsreport$', 'manager.views.newsPost', name='newsPost'),
    # 上传总结
    url(r'^manager/\d+/summarypost$', 'manager.views.summaryPost', name='summaryPost'),
    # 统计信息
    url(r'^manager/statistic$', 'manager.views.managerStatistic', name='managerStatistic'),
    # 服务队社团汇总页
    url(r'^manager/all$', 'manager.views.managerAllList', name='managerAllList'),


    # 全部新闻列表
    url(r'^news_all/$', 'news.views.newsList', name='newsList'),
    # 新闻详情页
    url(r'^news/\d+$', 'news.views.newsDetail', name='newsDetail'),

    # 校青志首页
    url(r'^xqz/\d+/home$', 'xqz.views.home', name='xqzHomePage'),
    # 校青志信息展示页
    url(r'^xqz/\d+$', 'xqz.views.xqzPage', name='xqzPage'),
    # 校青志活动审核页
    url(r'^xqz/\d+/activity/\d+$', 'xqz.views.xqzActivityDetail', name='xqzActivityDetail'),
    # 活动评比
    url(r'^xqz/\d+/award$', 'xqz.views.award', name='award'),

    # url(r'^Volunteer/', include('Volunteer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
