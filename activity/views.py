# coding=utf-8
from django.shortcuts import render_to_response

# 全部活动列表
def activityList(request):
    return render_to_response('activity/activity_all.html')

# 活动详情页
def activityDetail(request):
    return render_to_response('activity/act_id.html')

# 活动全部评价
def activityComment(request):
    return  render_to_response('activity/actmess_all.html')

# 活动全部成员
def activityMember(request):
    return  render_to_response('activity/actmember_all.html')
