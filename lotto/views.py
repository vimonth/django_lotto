from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm


# Create your views here.
def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos' : lottos}) #메인 리턴방식

def hello(request):
    return HttpResponse('<h1 style="color:red;">Hello, world!</h1>')

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST) #filled form

        if form.is_valid():
            lotto = form.save(commit = False) # commit = False : DB에는 저장 안하고 임시저장!
            #임시저장이 끝난 하나의 행을 반환함
            lotto.generate()

            return redirect('index_name')

    else:
        form = PostForm() #empty form
        return render(request, 'lotto/form.html',{'form':form})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request, 'lotto/detail.html',{'lotto':lotto})
