from django.shortcuts import render

# Create your views here.
def index(request):
    print('index django')
    return render(request,'index.html')