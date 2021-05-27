import requests

LoginUrl=r'http://stu.ityxb.com/back/bxg_anon/login'
InfoUrl=r'http://stu.ityxb.com/back/bxg_anon/user/loginInfo'
PointsUrl=r'http://stu.ityxb.com/back/bxg/user/getThreeRedPoints'
UnfinshedUrl=r'http://stu.ityxb.com/back/bxg/user/unfinished'
PreViewUrl=r'http://stu.ityxb.com/back/bxg/preview/info'
PreViewUpdateUrl=r'http://stu.ityxb.com/back/bxg/preview/updateProgress'
QuestionRul=r'http://stu.ityxb.com/back/bxg/preview/questions'
QuestionsUpdateUrl=r'http://stu.ityxb.com/back/bxg/preview/ansQuestions'
QuestionsView=r'http://stu.ityxb.com/back/bxg/preview/viewQuesAnsResult'
cookies = ""

def _Post(url,data={}):
    header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        'cookie' : "JSESSIONID=%s;"%cookies
    }
    return requests.post(url,headers=header,data=data).json()

def GetInfo():
    return _Post(InfoUrl)

def GetPoint():
    return _Post(PointsUrl)['resultObject']

def GetUnished():
    data={
        'pageNumber':'1',
        'pageSize':'10',
        'type':'1'
    }
    return _Post(UnfinshedUrl,data)['resultObject']

def GetPreviemInfo(id):
    data={
        'previewId':id
    }
    return _Post(PreViewUrl,data)['resultObject']

def UpdatePoint(previewId,pointId,s):
    data={
        'previewId':previewId,
        'pointId':pointId,
        'watchedDuration':s
    }
    return _Post(PreViewUpdateUrl,data)

def GetQuestions(previewId,pointId):
    data={
        'previewId':previewId,
        'pointId':pointId,
    }
    try:
        return _Post(QuestionRul,data)['resultObject'][0]['id']
    except:
        return 0

def UpdateQuestions(previewId,pointId,QuestionId,answer):
    data={
        'previewId':previewId,
        'pointId':pointId,
        'preivewQuestionId':QuestionId,
        'stuAnswer':answer,
    }
    a = _Post(QuestionsUpdateUrl,data)
    return a;

def GetAnswer(previewId,pointId):
    data={
        'previewId':previewId,
        'pointId':pointId,
    }
    a = _Post(QuestionsView,data)
    return a['resultObject'][0]['answerOriginal']

def LoginCookies(username,password):
    data={
        'automaticLogon':'false',
        'username':username,
        'password':password
    }
    info=requests.post(LoginUrl,data)
    return info.cookies['JSESSIONID']
