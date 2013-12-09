# coding=utf-8
from django.shortcuts import render_to_response

# 全部新闻列表
def newsList(request):
    return render_to_response('news/news_all.html')

# 新闻详情页
def newsDetail(request):
    return render_to_response('news/news_id.html')
