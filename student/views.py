from django.shortcuts import render, HttpResponseRedirect
from .forms import signupform, changepassform, EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash



# Create your views here.

# For home page.
def index(request):
    return render(request, 'index.html')


# For login page.
def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login Successfully...')
                    return HttpResponseRedirect('userprofile')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form':fm})
    else:
        return HttpResponseRedirect('userprofile')
    
# For signup page.
def usersignup(request):
    if request.method == "POST":
        fm = signupform(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully...')
            fm.save()
    else:
        fm = signupform()
    return render(request, 'signup.html', {'form':fm})

# For profile page.
def userprofile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = EditUserProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                messages.success(request, 'Profile Updated...')
                fm.save()
        else:
            fm = EditUserProfileForm(instance=request.user)
        return render(request, 'profile.html', {'name':request.user, 'lastlogin':request.user.last_login, 'form':fm})
    else:
        return HttpResponseRedirect('/login')

# For logout.
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login')

# For Change Password with old password.
def userchgpass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = changepassform(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password Change Successfully...')
                return HttpResponseRedirect('/userprofile')
        else:
            fm = changepassform(user=request.user)
        return render(request, 'changepassword.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login')