from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')

        user = None
        if '@' in username_or_email:
            try:
                user_obj = User.objects.get(email=username_or_email)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                pass
        else:  
            user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username/email or password.")
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return render(request, 'signup.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        login(request, user)
        return redirect('dashboard')
    
    return render(request,'signup.html')

def forgotPassword(request):
   return redirect('password_reset')

@login_required
def dashboard(request):
   return render(request,'dashboard.html')

@login_required
def profile(request):
   return render(request,'profile.html')

@login_required
def changePassword(request):
   if request.method == 'POST':
        oldpassword = request.POST.get('oldPassword')
        newPassword = request.POST.get('newPassword')
        
        user = request.user

        if not user.check_password(oldpassword):
            messages.error(request, "Old password is incorrect.")
            return render(request, 'change-password.html')
        
        if oldpassword == newPassword:
            messages.error(request, "New password cannot be the same as the old password.")
            return render(request, 'change-password.html')
        
        user.set_password(newPassword)
        user.save()

        update_session_auth_hash(request, user)
        
        messages.success(request, "Your password has been updated successfully.")
   
   return render(request,'change-password.html')