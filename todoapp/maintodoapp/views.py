#
#
#
from django.shortcuts import render


# data --->
tasks = [
        {'id': 1,
         'task': 'Sa merg la mare',
         'status_task': True
         },

        {'id': 2,
         'task': 'Sa cumpar paine',
         'status_task': False
         },

        {'id': 3,
         'task': 'Sa citesc',
         'status_task': False
         },

        {'id': 4,
         'task': 'Sa fac meditatii',
         'status_task': True
         }
    ]


def home(request):
    context = {'tasks': tasks}
    return render(request, 'maintodoapp/home.html', context)


def about(request):
    return render(request, 'maintodoapp/about.html')
