# coding=utf-8
# users sub-system
from django.shortcuts import render_to_response

# 活动组织方首页
def home(request):
    return render_to_response('manager/home.html')

# 活动组织方信息展示页（面向用户）
def managerInfo(request):
    return render_to_response('manager/user_id.html')

# 活动组织方活动列表页
def managerActivityList(request):
    return render_to_response('manager/manaact_all.html')

# 筛选志愿者
def checkVolunteer(request):
    return render_to_response('manager/checkvol.html')

# 更新志愿者时间
def timeUpdate(request):
    return render_to_response('manager/changetime.html')

# 申请活动
def activityPost(request):
    return render_to_response('manager/post.html')

# 发布新闻
def newsPost(request):
    return render_to_response('manager/news_report.html')

# 上传总结
def summaryPost(request):
    return render_to_response('manager/summarypost.html')

# 统计信息
def managerStatistic(request):
    return render_to_response('manager/statistic.html')

# 服务队社团汇总页
def managerAllList(request):
    return render_to_response('manager/managerall.html')
