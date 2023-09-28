from django.shortcuts import render


def greet(request):
    name = request.GET.get('name', '')
    message = request.GET.get('message', '')
    context = {'name': name, 'message': message}
    return render(request, 'greet.html', context)
