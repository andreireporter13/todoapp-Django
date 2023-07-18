#
#
#
from django.shortcuts import render
from .models import Tasks
from .forms import TasksForm


def home(request):
    if request.method == 'POST':
        form = TasksForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = TasksForm()
            tasks = Tasks.objects.all()
            context = {'form': form, 'tasks': tasks}
            return render(request, 'maintodoapp/home.html', context)
    else:
        form = TasksForm()
        tasks = Tasks.objects.all()
        context = {'form': form, 'tasks': tasks}
        return render(request, 'maintodoapp/home.html', context)


def about(request):
    return render(request, 'maintodoapp/about.html')
