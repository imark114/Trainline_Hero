from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import User
from .forms import SignUpForm, UpdateProfileForm
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.contrib.auth.forms import  PasswordChangeForm

# Create your views here.

def SignUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"https://trainline-hero-1.onrender.com/account/active/{uid}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html',{'confirm_link': confirm_link})
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            messages.success(request,"Check Your Email to Varify Account")
            return redirect('home')
    form = SignUpForm()
    return render(request, 'signup_form.html', {'form': form ,'type': 'SignUp'})

def activate(request,uid64,token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except (User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('signup')

class UserLoginView(LoginView):
    template_name = 'login_form.html'
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request,'Logged In Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request,'Given informations are incorrect')
        response = super().form_invalid(form)
        return response

    def get_context_data(self, **kwargs) -> dict[str]:
            context = super().get_context_data(**kwargs)
            context["type"] = 'Login'
            return context

class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class ProfileView(UpdateView):
    model = User
    form_class = UpdateProfileForm
    success_url = reverse_lazy('home')
    template_name = 'form.html'
    pk_url_kwarg='id'

    def form_valid(self, form):
        messages.success(self.request,'Profile Updated Successfully')
        return super().form_valid(form)
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["type"] = 'Update Profile'
        return context
    

class PassChangeView(PasswordChangeView):
    template_name = 'form.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Password Updated Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["type"] = 'Change Password'
        return context