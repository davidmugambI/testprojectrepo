from django.shortcuts import render,redirect
from django.http import HttpResponse
from demoapp.forms import demoform
from django.contrib import messages
from demoapp.models import demotable

# Create your views here.
def save_data(request):
    if request.method == 'POST':
        form = demoform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "data saved")
            return redirect('show')
            # return HttpResponse('saved')
    else:
        form = demoform()

    dict  =  {'form': form}
    return render(request, 'demoapp/form.html', dict)

def retrieve(request):
    data = demotable.objects.all()
    dict = {'data': data}
    return render(request, 'demoapp/display.html', dict)

def data_update(request,id):
    data = demotable.objects.get(id=id)
    if request.method == 'POST':
        form = demoform(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, 'updates')
            return redirect('show')
    else:
        form =  demoform(instance=data)
    dict = {'form': form}
    return render(request, 'demoapp/form.html', dict)

def data_delete(request,id):
    data = demotable.objects.get(id=id).delete()
    return redirect('show')

