from diary.models import Tag, Page, Diary
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView
from .forms import UserForm, CreateForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from social_django.models import UserSocialAuth
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import TemplateView
from django.urls import reverse


class IndexView(generic.ListView):
    template_name = 'diary/index.html'
    context_object_name = 'all_diarys'

    def get_queryset(self):
        """
        Return all of the objects in the list
        """
        return Page.objects.all()


class LoginView(UpdateView):
    template_name = 'registration/login.html'

    def dispatch(self, request):
        if request.user.is_authenticated:
            return redirect('diary:index')

        return render(request, 'registration/login.html')


class LogoutView(UpdateView):
    template_name = 'registration/logout.html'
    
    def dispatch(self, request):
        if request.user.is_authenticated:
            return render(request, 'registration/logout.html')

        return render(request, 'registration/login.html')

class CreateView(View):
    form_class = CreateForm
    template_name = 'diary/create.html'


class UserFormView(View):
    form_class = UserForm
    template_name = 'registration/registration_form.html'

    # display black form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return User objects if credential are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('')

        return render(request, self.template_name, {'form': form})
