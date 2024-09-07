from django.shortcuts import render
import random
# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def password(request):

    length = int(request.GET.get('length'))

    characters = list('abcdefghijklmnopqrstuvwxyz')
    password = ''

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWYZ'))
    if request.GET.get('special'):
        characters.extend(list('@[]{+*}!^¿?$%&/()ª|#~€¬'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for _ in range(length):
        password += random.choice(characters)

    return render(request, 'password.html', {'password_generator':password})
"""
from django.shortcuts import render
from django.views import View
import random
import string

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')

class PasswordView(View):
    def get(self, request):
        return render(request, 'password.html', {'password_generator': ''})

    def post(self, request):
        length = int(request.POST.get('length'))
        use_uppercase = request.POST.get('uppercase') == 'on'
        use_special = request.POST.get('special') == 'on'
        use_digits = request.POST.get('digits') == 'on'

        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        special_characters = "@[]{+*}!^¿?$%&/()ª|#~€¬"
        digits = string.digits

        characters = list(lowercase_letters)
        if use_uppercase:
            characters.extend(uppercase_letters)
        if use_special:
            characters.extend(special_characters)
        if use_digits:
            characters.extend(digits)

        password = ''.join(random.choices(characters, k=length))

        return render(request, 'password.html', {'password_generator': password})
"""