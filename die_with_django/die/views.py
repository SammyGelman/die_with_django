from django.shortcuts import render

# Create your view

import random

def roll_die(request):
    roll_result = None # Default
    if request.method == 'POST':
        roll_result = random.randint(1, 6)  # Random number between 1 and 6
    return render(request, 'die/roll_die.html', {'roll_result': roll_result})
