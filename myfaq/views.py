from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
import uuid
import json
from . import models
models.angelo_db



def index(request):

    return render(request, 'index.html',{'head':''})


# 提交内容接受函数
@csrf_exempt
def create_question(request):
    qtitle = request.POST.get('qtitle')
    qcontents = request.POST.get('qcontents')
    type = request.POST.get('type')
    # with open('t1232131.log','a+') as fl:
    #         fl.write(str(type))
    if qtitle =='' or qcontents =='':
        return HttpResponse('<font size="3" color="#FFFFFF">标题或者内容不能为空!！</font></center>'
                            ' </br><center><input type="submit" value="返回上一页" style="color: #FFFFFF;width:80px; height:30px;border:0.3px solid #000; background-color:#2B2F33"; onclick="javascript:history.back(-1)"></center>')

    try:
        uuids =str(uuid.uuid1())
        if qtitle is not None and qcontents is not None:
            sql= 'insert into question values( null, %s,%s,%s)'

            sql2 = 'insert into question_dill values( null, %s, %s )'
            # with open('t2.log','a+') as fl:
            #     fl.write(str(sql))
            models.angelo_db.query(sql,(qtitle,uuids,type))
            models.angelo_db.query(sql2,(qcontents, uuids))
        # if qcontents is not None:
        #     sql= 'insert into question_dill values( null, "%s", "%s" )'% (qcontents,uuids)
        #     with open('t1.log','a+') as fl:
        #         fl.write(str(sql))
        #     models.angelo_db.query(sql)
        return HttpResponse('<center><font size="3" color="#FFFFFF">提交成功！</font></center>'
                            ' </br><center><input type="submit" value="返回上一页" style="color: #FFFFFF;width:80px; height:30px;border:0.3px solid #000; background-color:#2B2F33"; onclick="javascript:history.back(-1)"></center>')
        # with open('t.log','a+') as fl:
        #     #     fl.write(str(qtitle)+'\n'+str(qcontents))
    except Exception as e:
        return HttpResponse(e)



#读取数据库，标题列表 LOMS
def loms_list_view(request):
    sql=  'select a.title,b.contents from question a join question_dill b on a.uuid = b.question_uuid and a.type =1 '
    result = models.angelo_db.query_all(sql)
    tit=[]
    con = []

    for i in result:

        tit.append(i[0])



    """
    循环出问题标题和内容
    for i in result:
        strs = '"'+i[0]+'":"'+i[1]+'"'
        x.append(strs)
    strs = ','.join(x)
    strs = '{'+strs+'}'
    # with open('t8.log', 'a+') as fl:
    #     fl.write( strs)
    strs=json.loads(strs, strict=False)
    # with open('t6.log', 'a+') as fl:
    #     fl.write(str(type(strs)))
    """
    x=[]

    data ={
        'tit':tit ,
        'con':tit,
    }
    return render(request,'loms_list_view.html',data)


#读取数据库，标题列表 itm
def itm_list_view(request):
    sql=  'select a.title,b.contents from question a join question_dill b on a.uuid = b.question_uuid and a.type =2 '
    result = models.angelo_db.query_all(sql)
    tit=[]
    con = []

    for i in result:

        tit.append(i[0])



    """
    循环出问题标题和内容
    for i in result:
        strs = '"'+i[0]+'":"'+i[1]+'"'
        x.append(strs)
    strs = ','.join(x)
    strs = '{'+strs+'}'
    # with open('t8.log', 'a+') as fl:
    #     fl.write( strs)
    strs=json.loads(strs, strict=False)
    # with open('t6.log', 'a+') as fl:
    #     fl.write(str(type(strs)))
    """
    x=[]

    data ={
        'tit':tit ,
        'con':tit,
    }
    return render(request,'itm_list_view.html',data)


#读取数据库，标题列表  twms
def twms_list_view(request):
    sql=  'select a.title,b.contents from question a join question_dill b on a.uuid = b.question_uuid and a.type =3 '
    result = models.angelo_db.query_all(sql)
    tit=[]
    con = []

    for i in result:

        tit.append(i[0])



    """
    循环出问题标题和内容
    for i in result:
        strs = '"'+i[0]+'":"'+i[1]+'"'
        x.append(strs)
    strs = ','.join(x)
    strs = '{'+strs+'}'
    # with open('t8.log', 'a+') as fl:
    #     fl.write( strs)
    strs=json.loads(strs, strict=False)
    # with open('t6.log', 'a+') as fl:
    #     fl.write(str(type(strs)))
    """
    x=[]

    data ={
        'tit':tit ,
        'con':tit,
    }
    return render(request,'twms_list_view.html',data)
# def  loms_content_list(request,con_id):
#
#     return HttpResponse(con_id)


#内容详情
def loms_book_detail(request, book_id, catgray):
    sql = 'select a.title,b.contents from question a join question_dill b on a.uuid = b.question_uuid and a.type =1'
    result = models.angelo_db.query_all(sql)
    tit = []
    con = []
    catgray=int(catgray)-1
    for i in result:
        contents = i[1].replace('\n', '<br />')
        con.append(contents)
        tit.append(i[0])

    text = '<font size="3" color="#FFFFFF">'+'<h2>'+tit[catgray]+'</h2>' +'<br />' +con[catgray] +'</font>'
    return HttpResponse(text+' </br><center><input type="submit" value="返回上一页" style="color: #FFFFFF;width:80px; height:30px;border:0.3px solid #000; background-color:#2B2F33"; onclick="javascript:history.back(-1)"></center>')


#内容详情 ITM
def itm_book_detail(request, book_id, catgray):
    sql = 'select a.title,b.contents from question a join question_dill b on a.uuid = b.question_uuid and a.type =2'
    result = models.angelo_db.query_all(sql)
    tit = []
    con = []
    catgray=int(catgray)-1
    for i in result:
        contents = i[1].replace('\n', '<br />')
        con.append(contents)
        tit.append(i[0])

    text = '<font size="3" color="#FFFFFF">'+'<h2>'+tit[catgray]+'</h2>' +'<br />' +con[catgray] +'</font>'
    return HttpResponse(text+' </br><center><input type="submit" value="返回上一页" style="color: #FFFFFF;width:80px; height:30px;border:0.3px solid #000; background-color:#2B2F33"; onclick="javascript:history.back(-1)"></center>')


#内容详情 TWMS
def twms_book_detail(request, book_id, catgray):
    sql = 'select a.title,b.contents from question a join question_dill b on a.uuid = b.question_uuid and a.type =3'
    result = models.angelo_db.query_all(sql)
    tit = []
    con = []
    catgray=int(catgray)-1
    for i in result:
        contents = i[1].replace('\n', '<br />')
        con.append(contents)
        tit.append(i[0])

    text = '<font size="3" color="#FFFFFF">'+'<h2>'+tit[catgray]+'</h2>' +'<br />' +con[catgray] +'</font>'
    return HttpResponse(text+' </br><center><input type="submit" value="返回上一页" style="color: #FFFFFF;width:80px; height:30px;border:0.3px solid #000; background-color:#2B2F33"; onclick="javascript:history.back(-1)"></center>')

def home(request):

    return render(request,'home.html')