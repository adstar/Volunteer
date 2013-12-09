# coding=utf-8
from django.shortcuts import render_to_response

# 校青志首页
def home(request):
    return render_to_response('xqz/home.html')

# 校青志信息展示页
def xqzPage(request):
    return render_to_response('xqz/user_id.html')

# 校青志活动审核页
def xqzActivityDetail(request):
    return render_to_response('xqz/act_id.html')

# 活动评比
def award(request):
    return render_to_response('xqz/award.html')
