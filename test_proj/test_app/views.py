from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView
from test_app.models import User
from .forms import SignUpForm, UserListForm
from datetime import date


class Index(TemplateView):
    """Index page"""
    template_name = "index.html"


class UsersList(ListView):
    """Users list page"""
    template_name = "users_list.html"
    model = User

    def dispatch(self, request, *args, **kwargs):
        self.form = UserListForm(request.GET)
        self.form.is_valid()
        return super(UsersList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = User.objects.all()
        if self.form.cleaned_data.get('search'):
            queryset = queryset.filter(first_name=self.form.cleaned_data['search'])
        if self.form.cleaned_data.get('search2'):
            queryset = queryset.filter(last_name=self.form.cleaned_data['search2'])
        if self.form.cleaned_data.get('sort_field'):
            queryset = queryset.order_by(self.form.cleaned_data['sort_field'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(UsersList, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context


class SignUp(CreateView):
    """Sign up page"""
    model = User
    template_name = "sign_up.html"
    form_class = SignUpForm
    success_url = "/users_list/"


class UserDetail(DetailView):
    """User detail page"""
    model = User
    template_name = 'user_detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.user = User.objects.get(pk=self.kwargs['pk'])
        return super(UserDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserDetail, self).get_context_data(**kwargs)
        context['age'] = ((date.today()).year - (self.user.birth_date).year)
        return context


class UserDelete(DeleteView):
    """User delete page"""
    model = User
    template_name = "user_delete.html"
    success_url = '/users_list/'
