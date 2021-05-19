from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import *
from .models import *
from django.http import HttpResponse
from django.core.files.storage import  FileSystemStorage
import random
from .models import Role_choices
from django.template.loader import render_to_string
from django.core.mail import send_mail
import json, requests

def home(request):  
    return render(request,"index.html",)

def about_us(request):  
    return render(request,"about.html",)

def contact_us(request): 

    if request.method =='POST':
        name=request.POST["name"]
        email=request.POST["email"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        send_mail(
           f"Message from {name}",
           message,
           email,
           ['testerwebsite007@gmail.com'],
           fail_silently=False
        )
        context={'name':name,}
        return render(request,"contact.html",context)
    context={}
    return render(request,"contact.html",context)

def privacy(request):  
    return render(request,"privacypolicy.html",)

def apply(request):
    # num=random.randrange(1121,9899)
    # global str_num
    # str_num=str(num)    
    # return render(request,"apply.html", {"cap":str_num})
    
    context = {
        
    }
    return render(request, "apply.html", context)

def apply_submit(request):
    
    name= request.POST['Name']
    email_id= request.POST['Email_id']
    years_of_experience=request.POST['Years_of_Experience']
    linkedin_profile= request.POST['Linkedin_Profile']
    expected_hourly_rate=request.POST['Expected_hourly_rate']
    resume= request.FILES['Resume']
    clientkey=request.POST['g-recaptcha-response']
    secretkey='6LeQsNsaAAAAAH4ckMnBLNWMWWnBNbWMAGqJvERR'
    capthchaData={
        'secret':secretkey,
        'response':clientkey,
        }
    r=requests.post( 'https://www.google.com/recaptcha/api/siteverify', data=capthchaData)
    response=json.loads(r.text)
    verify=response['success']
    fs=FileSystemStorage()
    fs.save(resume.name, resume)
    Cand = Candidate(Name=name,Email_id=email_id,Years_of_Experience=years_of_experience,Linkedin_Profile=linkedin_profile,
                    Expected_hourly_rate=expected_hourly_rate, Resume= resume,)  
    Cand.save()
    
        # if str(cap)==str_num :
        #     # return render(request, 'jobs.html',context)
        #     return HttpResponse("<h4>YOUR APPLICATION HAS BEEN SUBMITED SUCCESSFULLY</h4>")
        # else:
        #     return HttpResponse("<h4>Error captha</h4>") 
    if verify:
        return HttpResponse('<script>alert("sucess");</script>')
    else:
        return HttpResponse('<script>alert("not sucess");</script>') 
    context = {'name':name} 
    return render(request, "apply.html",)

        
def jobs(request):
    job_list= Job.objects.all()
    roles= Role.objects.all()
    locations= Location.objects.all()
    # products = myFilter.qs
    data = {'job_list':job_list,'roles':roles,'locations':locations}
  

    return render(request,'jobs.html',data)    
#def jobs_details(request):
#    job_des= Job.objects.all()
#    context={'jobs_details': job_des}
#    return render(request,'jobs_details.html',context=context)
def jobs_details(request,id):
   
    job_list_1=get_object_or_404(Job,pk=id)
    
    return render(request,'jobs_details.html',{'jobs_1':job_list_1})

def jobs_filter(request):
    roles=request.GET.getlist('role[]')
    print(roles)
    locations=request.GET.getlist('location[]')
    print(locations)
    jobsall=Job.objects.all().order_by('-id').distinct()
    print(jobsall)
    if len(roles)>0:
        jobsall=jobsall.filter(role__id__in=roles).distinct()
    if len(locations)>0:
        jobsall=jobsall.filter(location__id__in=locations).distinct()
  
    t=render_to_string('jobs_filter.html',{'data':jobsall})
    return JsonResponse({'data':t})

# def jobs_filter(request):
#     f = JobFilter(request.GET, queryset=Job.objects.all())
#     return render(request, 'jobs.html', {'filter': f})