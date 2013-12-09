# coding=utf-8
# users sub-system
from django.shortcuts import render_to_response, RequestContext
from database.models import ActivityInfo, CommonUser, Institution, ActivityNews
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
# from django.core.exceptions import DoesNotExist
import random
from django.contrib.auth import authenticate, login, logout

# 网站首页
def home(request):
    # 已完成活动 取前4项
    actFinished = ActivityInfo.objects.all().filter(act_check='CD').order_by('act_time')[:4]
    # 未完成活动（当前活动） 取前4项
    actUnFinished = ActivityInfo.objects.all().filter(act_check='CU').order_by('act_time')[:8]
    # Slider新闻
    sliderNews = ActivityNews.objects.all()[:4]

    return render_to_response('index.html', {'activityFinished': actFinished, 'activityUnFinished': actUnFinished, 'activityNews': sliderNews})

# 登陆处理
def loginInit(request):
    return render_to_response('login.html')
# 登陆页面
def loginHandler(request):
    username = request.POST['username']
    password = request.POST['password']
    if request.user.is_authenticated():
        return HttpResponse("您已经登陆。")
    else:
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("登陆成功。 ")
            else:
                return HttpResponse("该账户尚未激活，请激活后获得所有权限。")
        else:
            return HttpResponse("您输入的用户名或密码有误，请重试。")
# 登出页面
def logoutInit(request):
    return render_to_response('logout.html')
# 登出处理
def logoutHandler(request):
    if not request.user.is_authenticated():
        return HttpResponse("您尚未登录。")
    else:
        logout(request)
        return HttpResponse("退出成功。")
# 注册页面
def registerInit(request):
    # generaate check number for registration
    checkNum = random.randint(1,1000)
    return render_to_response('register.html', {'checkNum': checkNum}) 
# 注册处理
def registerHandler(request):
    id, userName, password, againPassword, tel, email, dept = '','', '', '', '', '', ''
    if 'userID' in request.POST:
        id = request.POST['userID']
    if 'userName' in request.POST:
        userName = request.POST['userName']
    if 'userPass' in request.POST:
        password = request.POST['userPass']
    if 'againUserPass' in request.POST:
        againPassword = request.POST['againUserPass']
    if 'tel' in request.POST:
        tel = request.POST['tel']
    if 'email' in request.POST:
        email = request.POST['email']
    if 'dept' in request.POST:
        dept = request.POST['dept']

    # check if password entered are the same
    if password != againPassword:
        return HttpResponse("您两次输入的密码不一致。")

    if id!='' and userName!='' and password!='' and tel!='' and email!='' and dept!='':
        # get the institution instance
        d = Institution.objects.get(inst_name=dept)

        # add user to the admin user model
        u = User.objects.create_user(id, email, password)
        u.is_active = False
        u.first_name = userName

        # add user to the database user model
        muser = CommonUser(user=u, cu_tel=tel, dept_id=d, password1=password)
        # save muser
        muser.save()
        # save user u
        u.save()

        # send email
        try:
            send_mail('Welcom to SCU Volunteer', "Welcome to SCU Volunteer. Click <a href='#'>here</a> to login.", 'volunteer@scu.edu.cn', [email], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('邮件发送失败。')
        # redirect to login page
        return HttpResponse('请登陆邮箱激活账户。')
    else:
        return HttpResponse("请将表单填写完整。")

# 重置密码页面
def resetPasswordInit(request):
    return render_to_response('resetpassword.html')
# 重置密码处理
def resetPasswordHandler(request):
    # check empty
    email = ''
    if 'user_email' in request.POST:
    # get user password, email
        email = request.POST['user_email']
        if email=='':
            return HttpResponse("请输入邮箱地址。")
        else:
            try:
                user = User.objects.get(email=email)
                password = CommonUser.objects.get(user=user).password1
                # send email
                # try:
                send_mail('SCU Volunteer', ':%s' % password, 'volunteer@scu.edu.cn', [email], fail_silently=False)
                return HttpResponse("密码已发送至您的邮箱。")
                # except BadHeaderError:
                    # return HttpResponse('邮件发送失败。')
            except User.DoesNotExist:
                return HttpResponse("邮箱地址不存在，请重新输入。")
    else:
        return HttpResponse("表单提交错误。")

# 志愿者个人主页
def userPage(request):
    return  render_to_response('user/user_id.html')

# 志愿者更改个人信息页
def userInfoChange(request):
    return render_to_response('user/info_change.html')

# 志愿者参加过的活动列表
def userActivityList(request):
    return render_to_response('user/useract_all.html')

# 志愿者的留言列表
def userMessageList(request):
    return render_to_response('user/usermessage_all.html')

# 志愿者的广播列表
def userBroadcastList(request):
    return render_to_response('user/userbroadcast_all.html')
