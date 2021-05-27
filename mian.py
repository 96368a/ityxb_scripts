import API
import traceback

username='157XXXXXXXX'#手机号码
password='123456'#密码

#可以直接填cookies值，填了cookies就不用填账号密码了，就是cookies可能每次都有手动填
API.cookies = ""

#登录信息
try:#检查cookies
    info=API.GetInfo()
    #尝试使用用户名密码登录
    if info['resultObject']==None:
        API.cookies=API.LoginCookies(username,password)
        info=API.GetInfo()['resultObject']
    print("登录成功，欢迎:%s"%info['nickname'])
    print("+++准备获取任务+++")
except:
    print("出现错误,请检查网络!!")
    exit(0)
#获取剩余完成任务
try:
    unfinshed=API.GetPoint()
    print('任务获取成功')
    previews=unfinshed['preview']
    previewids = []
    if previews>0:
        print('获取到任务，准备请求')
        previewpoint=API.GetUnished()['items']
        for pointinfo in previewpoint:
            previewids.append(pointinfo['id'])
    else:
        print("无任务！！")
        exit(0)
except:
    print("出现错误")
    exit(0)

#开始请求任务
try:
    for id in previewids:
        preview=API.GetPreviemInfo(id)
        print("准备开始请求任务：\n%s"%preview['preview']['previewName'])
        for preview_s in preview['chapters']:
            for ponint in preview_s['points']:
                print("请求: %s - %s"%(preview_s['chapter']['point_name'],ponint['point_name']))
                pointid=ponint['point_id']
                pushinfo=API.UpdatePoint(id,pointid,9999)
                # pushinfo={'success':'1','resultObject':"233"}
                if pushinfo['success']:
                    print("请求成功，当前观看时间:%s"%pushinfo['resultObject'])
                    print("准备请求题目")
                    questionsid=API.GetQuestions(id,pointid)
                    # questionsid=0
                    #提交题目
                    if questionsid!=0:
                        API.UpdateQuestions(id,pointid,questionsid,0)
                        #查看答案
                        answer=API.GetAnswer(id,pointid)
                        print("获取到答案%s,提交->"%chr(int(answer)+65))
                        if answer!=0:
                            API.UpdateQuestions(id,pointid,questionsid,answer)
                    else:
                        print("没有题目，跳过")          
                else:
                    print("请求失败")
except:
    print(traceback.format_exc())
    print("出现错误")
    exit(0)
