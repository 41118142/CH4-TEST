from django.shortcuts import render
from studentsapp.models import student

def listone(request): 
    try: 
        unit = student.objects.get(cName="林宸宇")  # 讀取一筆資料
    except:
        errormessage = " (讀取錯誤!)"
        unit = None
    return render(request, "listone.html", locals())

def listall(request):  
    students = student.objects.all().order_by('id')  # 全部資料
    return render(request, "listall.html", {'students': students})

def index(request):  
    students = student.objects.all().order_by('id')  # 首頁顯示全部
    return render(request, "index.html", {'students': students})
