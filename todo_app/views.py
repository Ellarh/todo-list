from django.core.paginator import Paginator
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import TodoList
from .forms import TodoListForm
from django.utils import timezone
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = 'index.html'


class CompletedTaskView(ListView):
    model = TodoList
    context_object_name = 'completed_tasks'
    template_name = 'completed_tasks.html'
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        return TodoList.objects.filter(task_is_done=True, user=user).order_by("-task_date")


class CreateTaskView(LoginRequiredMixin, CreateView):
    form_class = TodoListForm
    template_name = 'create_task.html'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = TodoList
    fields = ('task', 'task_description', 'task_is_done')
    template_name = 'update_task.html'


class DetailTaskView(DetailView):
    model = TodoList
    template_name = 'todo_list_detail.html'
    context_object_name = 'task_detail'


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = TodoList
    success_url = reverse_lazy('tasks')
    template_name = 'confirm_delete.html'


@login_required
def user_tasks(request):
    user = request.user
    tasks = TodoList.objects.filter(user=user).order_by('-task_date')
    return render(request, 'todo_list.html', context={'tasks': tasks})


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = RegisterForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return redirect('tasks')
        else:
            print(user_form.errors)
    else:
        user_form = RegisterForm()

    context = {
        'form': user_form,
        'registered': registered
    }

    return render(request, 'register.html', context=context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('tasks')
            else:
                return redirect('register')
        else:
            return HttpResponse('You have no account! Register.')
    else:
        return render(request, 'login.html', context={})


@login_required
def user_logout(request):
    logout(request)
    return redirect('tasks')
