from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from ringer.forms import RingerLoginForm
from ringer.models import Ringer
# Create your views here.
class RingerLoginView(View):
    """Creates an instance of controller for  Ringer Login.
       The class will authenticate user and then login the user. This is done by
       making get request to load login interface, then post request to
       authenticate and login. post method will redirect user to
       'ringer_profile' url.

       Attributes:
       template_name -- template to render login interface.
       form -- form class to load the login form.
    """
    template_name = 'ringer/login.html'
    form = RingerLoginForm
    def get(self,request):
        """add unbound form to the context and pass to render"""
        context = {
            'form': self.form()
        }
        return render(request,self.template_name,context)

    def post(self,request):
        """authenticate user and login if user valid. Redirect to
        ringer_profile"""
        form = self.form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password']
            user = authenticate(username = username, password = raw_password)
            if user is not None:
                login(request,user)
                return redirect('ringer_profile')

class RingerProfileView(LoginRequiredMixin, View):
    """Creates an instance of Profile controller. This class will show all the
       details related to Ringer model. get method will render a template with
       ringer info in the context. Ringer must be logged in to access this
       interface.

       Attributes:
       template_name -- template to render profile interface.
       login_url -- url where user will be redirected if not logged in.
    """
    template_name = 'ringer/profile.html'
    login_url = '/ringer/login'

    def get(self,request):
        """This method will get Ringer instance using request user and
           add it to context
        """
        ringer = Ringer.objects.get(user=request.user)
        context = {
            'ringer': ringer,
        }
        return render(request,self.template_name,context)
