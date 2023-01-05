from http.client import HTTPResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Person


@csrf_exempt
def personal_page(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        context = {
            'persons': persons
        }
        return render(request, 'main.html', context)

    elif request.method == 'POST':
        form = Person(request.POST)
        if form.is_valid():
            person = Person()
            person.full_name = form.cleaned_data['full_name']
            person.height = form.cleaned_data['height']
            person.gender = form.cleaned_data['gender']
            person.age = form.cleaned_data['age']
            person.save()
            return HTTPResponse(person, status=201)
        else:
            return HTTPResponse('Error', status=400)
