from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import UserInfo
from django.contrib.auth.mixins import LoginRequiredMixin


class UserInsertForm(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = UserInfo
    fields = '__all__'
    success_url = "/"
    template_name = 'userdata/form.html'


class Home(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    model = UserInfo
    context_object_name = "data"
    template_name = 'userdata/home.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page_title'] = 'home page'
        return data


class UpdateUserInfo(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = UserInfo
    fields = '__all__'
    success_url = "/"
    template_name = 'userdata/form.html'


class DeleteUserInfo(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    model = UserInfo
    # context_object_name = 'delete-userinfo'
    success_url = "/"
    template_name = 'userdata/delete-userinfo.html'
