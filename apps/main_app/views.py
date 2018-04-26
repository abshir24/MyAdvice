from django.shortcuts import render,redirect
from ..logreg.models import User
from .models import Answers
from django.contrib import messages
import random

# Create your views here.

def home(request):
    return render(request,'main_app/home.html')

def answer(request):
    return render(request,'main_app/addanswer.html')

def addAnswer(request):
    newanswers = []
    for key in request.POST.keys():
        if "csrf" in key:
            continue
        for value in request.POST.getlist(key):
            newanswers.append(value)
    Answers.objects.answerAdd(newanswers, request.session["user_id"])
    return redirect('main:home')

def newquestion(request):
    user = User.objects.get(id = request.session["user_id"])
    useranswers = Answers.objects.filter(user = user)
    count  = 0
    for key in useranswers:
        count = count + 1
    random_num = random.randint(0,count-1)

    messages.error(request, useranswers[random_num].answer)

    return redirect('main:home')
