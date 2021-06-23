from django.shortcuts import render,HttpResponse,redirect
from .models import post
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, profileUpdateForm
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
posts=[
    {
        'author':'Zorag',
        'title':'post1',
        'content':'something1',
        'date':'17th june'
    },
    {
        'author':'sporag',
        'title':'post2',
        'content':'something2',
        'date':'16th june'
    }
]
def sumpott(request):
    return render(request,'blog1/sumpott.html')
    
def index(request):
    context={
        'posts':post.objects.all()
    }
    return render(request,'blog1/index.html',context)

class postlistview(ListView):
    model=post
    template_name='blog1/index.html'
    context_object_name='posts'
    ordering=['-date']

class postcreateview( LoginRequiredMixin,CreateView):
    model=post
    fields=['title','contents']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

def about(request):
    return render(request,'blog1/about.html')  

def register(request):
    if request.method=='POST':
         form=UserRegisterForm(request.POST)
         if form.is_valid():
             form.save()
             username=form.cleaned_data.get('username')
             messages.success(request,f'account created for {username}!')
             return redirect('blog1_index')
    else:
         form=UserRegisterForm()     
   
    return render(request,'blog1/register.html',{'form':form})
@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=profileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('/')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=profileUpdateForm(instance=request.user.profile)  
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'blog1/profile.html',context)    

