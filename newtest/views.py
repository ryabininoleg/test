from django.shortcuts import render

from .models import Name


def name(request):

    global names
    if request.POST:
        names = request.POST.dict()
        del names['csrfmiddlewaretoken']
        

    return render(request, 'template.html', locals())

def result(request):
	
     Name.objects.create(data=names)
     all_names = Name.objects.all()

     return render(request, 'result.html', locals())


