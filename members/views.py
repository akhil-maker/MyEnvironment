from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm

# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'login.html'
    success_url = reverse_lazy('login')
    print("done")
    success_message = "You are successfully registered"
