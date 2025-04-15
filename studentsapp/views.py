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
from django.shortcuts import render
from studentsapp.models import student
from datetime import date

def initdata(request):
    if not student.objects.filter(cName="林宸宇").exists():
        student.objects.create(cName="林宸宇", cSex="M", cBirthday=date(2004,6,22),
                               cEmail="41118142@school.com", cPhone="0909777615", cAddr="鳥松區87號")
    return render(request, "index.html", {"students": student.objects.all()})
