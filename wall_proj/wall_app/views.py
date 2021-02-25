from django.shortcuts import render, redirect
from django.contrib import messages
from login_app.models import User

def wall_index(request):
    if not 'user_id' in request.session:
        messages.error(request, "You are not logged in.")
        return redirect("/")
    user_first_name = request.session['first_name']
    context = {
        "user_first_name": user_first_name
    }
    return render(request, "wall_index.html", context)