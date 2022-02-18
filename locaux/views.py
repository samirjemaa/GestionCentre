# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render

from locaux.forms import LocalForm


def home(request):
    context = {

    }
    return render(request, 'locaux/index.html', context)


def add_local(request):
    submitted = False
    if request.method == "POST":
        form = LocalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/locaux/add_local?submitted=True')
    else:
        form = LocalForm
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted
    }
    return render(request, 'locaux/add_local.html', context)
