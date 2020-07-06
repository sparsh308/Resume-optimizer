from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Developer_info ,UserProfile
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.core.files.base import ContentFile
import docx2txt
import xlrd
import os
def register(request):
    return render(request,"register.html")


def home(request):
    if(request.method=='POST'):
        username=request.POST.get("username", False)
        password=request.POST.get("password", False)
        email=request.POST.get("email", False)
        function=request.POST.get("function", False)
        salarybkt=request.POST.get("salarybkt", False)
        if(User.objects.filter(username=username).exists()):
            {
            messages.info(request,'Username Already Exist')
           
            }
        elif User.objects.filter(email=email).exists():
            {
             messages.info(request,'Email Already Exist')
             
            }
        else:
           
            user=User.objects.create_user(username=username,password=password,email=email)
            user.save()
            newUserProfile=UserProfile(function=function,salarybkt=salarybkt,user=user)
            newUserProfile.save()
            
           ## email=EmailMessage(
             ##   'hello thank you for sign up',
            ##    'hello thank you for sign up',
            ##    settings.EMAIL_HOST_USER,
            ##    [email],
           ## )
            
           ## email.send()
            print('usercreated')

        return redirect('/home')
    else:    
        devs=Developer_info.objects.all()

        return render(request,"index.html",{'devs':devs})

def app_page(request):
    if(request.method=='POST'):
        username=request.POST.get("username1", False)
        password=request.POST.get("password1", False)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            devs=Developer_info.objects.all()

            return render(request,"index.html",{'devs':devs})

        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/#footer')
    else:
      

        return render(request,"main.html")

def logout(request):
    auth.logout(request)
    return redirect('/')




def Application(request):
       
    if(request.method=='POST'):
        uploaded_file=request.FILES['document']
        print(uploaded_file.name)
        kk=FileSystemStorage(location=settings.MEDIA_ROOT1)
        kk.save('resume.docx',uploaded_file)
        user=UserProfile.objects.get(user_id=request.user.id)
        user.doc= uploaded_file
        user.save()


        jd=request.POST.get("jdbox")
        print(jd)
       
       

        loc = (os.path.join(settings.MEDIA_ROOT,'Data_base.xlsx'))

        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)

        # For row 0 and column 0
        sheet.cell_value(0, 0)
        list =[]
        for i in range(sheet.nrows):
    #       print(sheet.cell_value(i, 0))
            list.append(sheet.cell_value(i, 0))
        ulist = []
        for i in list:
            if i not in ulist:
                ulist.append(i)

        #print(len(list))
        #print(len(ulist))
        resume = docx2txt.process(os.path.join(settings.MEDIA_ROOT,'Appdata','resume.docx'))
        #print(resume[0:40])
        JD = jd
       
        #print(JD[0:40])

        job =  []
        res =  []
        datas=[]
        for x in ulist:
            boolean = x.lower() in JD.lower()

            if boolean == True:
                job.append(x.lower())
        for x in ulist:
            boolean = x.lower() in resume.lower()

            if boolean == True:
                res.append(x.lower())
        print("Jobs match", job)
        print("Resume match", res)


        missing = set(job) - set(res)
        for keyword in missing:
            datas.append(keyword)
        print("missing variables are : ", datas)
        os.remove(os.path.join(settings.MEDIA_ROOT, 'Appdata','resume.docx'))
        return render(request,"main.html",{'data':datas})