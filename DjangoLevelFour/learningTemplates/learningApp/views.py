from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'Hello World','number':100}
    return render(request,'learningApp/index.html',context_dict)

def other(request):
    return render(request,'learningApp/other.html')

def relative(request):
    return render(request,'learningApp/relativeUrl.html')
