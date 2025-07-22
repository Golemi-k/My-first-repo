from django.shortcuts import render
import random

def index(request):
    message = None

    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        guess = request.POST.get('guess')


        guess = int(guess)
        random_number = random.randint(1, 10)

        if guess == random_number:
            message = f"Brawo {user_name}! Trafiłeś liczbę {random_number}!"
        else:
            message = f"Niestety {user_name}, nie trafiłeś. Wylosowana liczba to {random_number}."



    return render(request, 'hello.html', {'message': message})
