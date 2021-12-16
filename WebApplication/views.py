from django.shortcuts import render

# Create your views here.
def trans(request):
    return render(request, "trans.html")

from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

def login (request):
    
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username,password=password)

      if user is not None:
          auth.login(request, user)
          return redirect("/")
         
      else:
          messages.info(request,'INVALID CREDENTIALS')
          return redirect('login')

   else:
        return render(request,'loogin.html')


# Create your views here.
def register (request):


    if request.method == 'POST':
         first_name = request.POST['first_name']
         last_name = request.POST['last_name']
         username = request.POST['username']
         password1 = request.POST['password1']
         password2 = request.POST['password2']
         email = request.POST['email']

         if password1==password2:
           if User.objects.filter(email=email).exists():
              messages.info(request,'Email already registered')
              return redirect('register')

           elif User.objects.filter(username=username).exists():
              messages.info(request,'Try any other username')
              return redirect('register')

           else:
              user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
              user.save();
              print('REGISTERED')
              return redirect('login')

         else:
           messages.info(request,'PASSWORDS DONT MATCH')
         return redirect('/')

    else :

      return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def profile (request):
    return render(request,'profile.html')

def average(request):   
     userid = None
     if request.user.is_authenticated:
         userid = request.user.id
         print(userid)
     dataset = graphinput.objects.filter(user=userid) \
        .values('Value1')
     
     a=dataset.aggregate(Sum('Value1'))
     b=dataset.aggregate(Avg('Value1'))
     print(a)
     print(b)

     

     avg = b.get('Value1__avg', 0)

     if avg < 90:
          messages.info(request,'Low fasting sugar ')
          
     elif avg > 110:
           messages.info(request,'High fasting sugar ')

     else:
          messages.info(request,'You are normal ')
    

   
     return render(request, 'profile.html')

from django.shortcuts import render,redirect
from WebApplication.models import graphinput
#from.utils import get_plot
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum,Avg
from django.db.models import Q


def index(request):

 if request.method == 'POST':
     JanMonth = request.POST['JanMonth']
     JanValue = request.POST['JanValue']
     
     JanValue2 = request.POST['JanValue2']

     FebMonth = request.POST['FebMonth']
     FebValue = request.POST['FebValue']
     FebValue2 = request.POST['FebValue2']

     MarMonth = request.POST['MarMonth']
     MarValue = request.POST['MarValue']
     MarValue2 = request.POST['MarValue2']

     AprMonth = request.POST['AprMonth']
     AprValue = request.POST['AprValue']
     AprValue2 = request.POST['AprValue2']

     MayMonth = request.POST['MayMonth']
     MayValue = request.POST['MayValue']
     MayValue2 = request.POST['MayValue2']

     JunMonth = request.POST['JunMonth']
     JunValue = request.POST['JunValue']
     JunValue2 = request.POST['JunValue2']

     JulMonth = request.POST['JulMonth']
     JulValue = request.POST['JulValue']
     JulValue2 = request.POST['JulValue2']

     AugMonth = request.POST['AugMonth']
     AugValue = request.POST['AugValue']
     AugValue2 = request.POST['AugValue2']

     SepMonth = request.POST['SepMonth']
     SepValue = request.POST['SepValue']
     SepValue2 = request.POST['SepValue2']

     OctMonth = request.POST['OctMonth']
     OctValue = request.POST['OctValue']
     OctValue2 = request.POST['OctValue2']

     NovMonth = request.POST['NovMonth']
     NovValue = request.POST['NovValue']
     NovValue2 = request.POST['NovValue2']

     DecMonth = request.POST['DecMonth']
     DecValue = request.POST['DecValue']
     DecValue2 = request.POST['DecValue2']

     userid = None
     if request.user.is_authenticated:
         userid = request.user.id
         print(userid)
         qs =graphinput.objects.filter(user_id=userid) 

         if qs.filter(Month=JanMonth).exists():
              messages.info(request,'January month already exist')
              return redirect('index')

         elif qs.filter(Month=FebMonth).exists():
              messages.info(request,'February month already exist')
              return redirect('index')

         elif qs.filter(Month=MarMonth).exists():
              messages.info(request,'March month already exist')
              return redirect('index')

         elif qs.filter(Month=AprMonth).exists():
              messages.info(request,'April month already exist')
              return redirect('index')

         elif qs.filter(Month=MayMonth).exists():
              messages.info(request,'May month already exist')
              return redirect('index')

         elif qs.filter(Month=JunMonth).exists():
              messages.info(request,'June month already exist ')
              return redirect('index')
 
         elif qs.filter(Month=JulMonth).exists():
              messages.info(request,'July month already exist')
              return redirect('index')

         elif qs.filter(Month=AugMonth).exists():
              messages.info(request,'August month already exist')
              return redirect('index')

         elif qs.filter(Month=SepMonth).exists():
              messages.info(request,'September month already exist')
              return redirect('index')

         elif qs.filter(Month=OctMonth).exists():
              messages.info(request,'October month already exist')
              return redirect('index')

         elif qs.filter(Month=NovMonth).exists():
              messages.info(request,'November month already exist')
              return redirect('index')

         elif qs.filter(Month=DecMonth).exists():
              messages.info(request,'December month already exist')
              return redirect('index')


      
     

         else:
            
            if JanValue != '' or JanValue2 !='':
             graphplot = graphinput.objects.create(Month=JanMonth,Value1=JanValue,Value2=JanValue2,user=request.user)
             graphplot.save();
            if FebValue != '':
             graphplot = graphinput.objects.create(Month=FebMonth,Value1=FebValue,Value2=FebValue2,user=request.user)
             graphplot.save();
            if MarValue != '':
             graphplot = graphinput.objects.create(Month=MarMonth,Value1=MarValue,Value2=MarValue2,user=request.user)
             graphplot.save();
            if AprValue != '':
              graphplot = graphinput.objects.create(Month=AprMonth,Value1=AprValue,Value2=AprValue2,user=request.user)
              graphplot.save();
            if MayValue != '':
             graphplot = graphinput.objects.create(Month=MayMonth,Value1=MayValue,Value2=MayValue2,user=request.user)
             graphplot.save();
            if JunValue != '':
             graphplot = graphinput.objects.create(Month=JunMonth,Value1=JunValue,Value2=JunValue2,user=request.user)
             graphplot.save();
            if JulValue != '':
             graphplot = graphinput.objects.create(Month=JulMonth,Value1=JulValue,Value2=JulValue2,user=request.user)
             graphplot.save();
            if AugValue != '':
             graphplot = graphinput.objects.create(Month=AugMonth,Value1=AugValue,Value2=AugValue2,user=request.user)
             graphplot.save();
            if SepValue != '':
             graphplot = graphinput.objects.create(Month=SepMonth,Value1=SepValue,Value2=SepValue2,user=request.user)
             graphplot.save();
            if OctValue != '':
             graphplot = graphinput.objects.create(Month=OctMonth,Value1=OctValue,Value2=OctValue2,user=request.user)
             graphplot.save();
            if NovValue != '':
             graphplot = graphinput.objects.create(Month=NovMonth,Value1=NovValue,Value2=NovValue2,user=request.user)
             graphplot.save();
            if DecValue != '':
             graphplot = graphinput.objects.create(Month=DecMonth,Value1=DecValue,Value2=DecValue2,user=request.user)
       
             graphplot.save();
            print('SUCCESFULLY ADDED')
            return redirect('ticket_class_view')
     else:
            return redirect('index')



 else:
    return render(request, 'bp.html')

def ticket_class_view(request):
     userid = None
     if request.user.is_authenticated:
         userid = request.user.id
         print(userid)
     dataset = graphinput.objects.filter(user=userid) \
        .values('Month') \
        .values('Value1')\
        .values('Month','Value1','Value2')
     print(dataset)
     return render(request, 'barchart.html', {'dataset': dataset})

from WebApplication.forms import EditForms
def display(request):
     userid = None
     if request.user.is_authenticated:
         userid = request.user.id
         print(userid)
     displays = graphinput.objects.filter(user=userid)
     print(displays)
     return render(request, 'display.html', {
        'displays': displays
        })

def editdisplay(request):
     userid = None
     if request.user.is_authenticated:
         userid = request.user.id
         print(userid)
     displaymonthvalue= graphinput.objects.filter(user=userid)
     return render(request,"edit.html",{
      'displaymonthvalue':displaymonthvalue
      })

def updatedisplay(request):
    user=''
    if request.user.is_authenticated:
        print(user)
        form = EditForms(request.POST)
 
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user

            print('ADDED SUCCESFULLY')
            return render(request,"edit.html",{'displaymonthvalue':displaymonthvalue})

        else:
           
           print("no such form")

    return redirect('display')

from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .forms import UploadForm
from .models import uploadfile

# Create your views here.
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

def list(request):
    lists = uploadfile.objects.all()
    return render(request, 'list.html', {
        'lists': lists
        })


def uploading(request):
    if request.method == 'POST':
        form = UploadForm (request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = UploadForm()
    return render(request, 'uploading.html', {
        'form': form
    })

def delete_book(request, pk):
    if request.method == 'POST':
        book = uploadfile.objects.get(pk=pk)
        book.delete()
    return redirect('list')
