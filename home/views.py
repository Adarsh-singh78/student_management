from django.shortcuts import render,redirect
from .models import student
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
# Create your views here.

# st=student.objects.all()

def home(request):
    search_query=request.GET.get('srch','')

    print(search_query)
    if search_query:
        sst=student.objects.filter(Q(name__icontains=search_query)|Q(email__icontains=search_query)|Q(mobile_no__icontains=search_query))
    else:
        sst=student.objects.all()
    context={
        'data':sst
    }
    return render(request,"first.html",context)

def sv(request):
    if request.method=="POST":
        nm=request.POST.get("name")
        email=request.POST.get("email")
        contact=request.POST.get("contact")
        """
            empty form will be saved in db->required and name.isalpha()
            integrity error will be given ->filter().exists()
            constraints and validations are different things and validation is not checked
            
        """
        print(nm,email,contact)
        if  not nm.isalpha() or student.objects.filter(mobile_no=contact).exists():
            messages.warning(request,"ERROR OCCURED")
            messages.success(request,"huehue")
            return redirect('home')

        else:
            messages.success(request,"SUSSESSFULLY CREATED")
            student.objects.create(name=nm,email=email,mobile_no=contact)
        return redirect('home')

def deleting(request):
    if request.method=="POST":
        a=request.POST.get("hid")
        st=student.objects.get(id=a)
        st.delete()
        return redirect('home')
    
def updates(request):
    if request.method=="POST":
        id=request.POST.get('hidup')
        # print(a)
        st=student.objects.get(id=id)
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        
        st.name=name
        st.email=email
        st.mobile_no=contact
        st.save()

        return redirect('home')
    return HttpResponse("huehue")


"""
    What are your Strength and your weaknesses ?

    1.  calcualte and analyze
    2.  console.log('hello world' )
"""