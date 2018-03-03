from django.shortcuts import render

# Create your views here.
def index(request):
    dictCtx ={'description':'this  is  just a description','number':90}
    return render(request,'basic_app/index.html',dictCtx)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
