from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


from .import forms
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def register(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}, your account has been created successfully, please login")
            return redirect('user-login')   
        
        
    else:
        form = forms.UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


    


@login_required()#decorator
def profile(request):
    return render(request, 'users/profile.html')



@permission_required('auth.add_user') # Example permission, replace with your desired permission code
def admin_view(request):
    # Only users with the 'auth.add_user' permission can access this view
    users = users.objects.all()
    return render(request, 'admin/users.html', {'users': users})

