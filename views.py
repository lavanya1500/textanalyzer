from django.shortcuts import render
# from .models import DemoModel
from django.http import HttpResponse
import re

# def DemoView(request):
#     return HttpResponse('''<h1>My Website</h1> <a href="https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/?ref=lbp"> Django GFG</a>''')

def DemoView2(request):
    return render(request, 'index.html')

def analyze(request):
    str= request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    caps= request.GET.get('capitalize','off')
    newline=request.GET.get('newLineRemover','off')
    extraSpace=request.GET.get('extraSpaceRemover','off')

    if removepunc=="on":
        result = re.sub(r'[^\w\s]', '',str )
        params={'purpose':'Removed Punctuations','analyzed_text':result}
        str=result
        # return render(request,'analyze.html',params)
    
    if caps=="on":
        result=""
        for i in str:
            result+=i.upper()
        params={'purpose':'UPPERCASE','analyzed_text':result}
        str=result
        # return render(request,'analyze.html',params)
    
    if newline=="on":
        result=""
        for i in str:
            if i!="\n":
                result+=i

        params={'purpose':'New line removed','analyzed_text':result}
        str=result
        # return render(request,'analyze.html',params)
    
    if extraSpace=="on":
        result=""
        for index,char in enumerate(str):
            if str[index]==" " and str[index+1]==" ":
                pass
            else:
                result+=char

        params={'purpose':'Extraspace Removed','analyzed_text':result}
        str=result
        # return render(request,'analyze.html',params)
    
    if(removepunc!="on" and caps!="on" and newline!="on" and extraSpace!="on"):
        return HttpResponse("Error")
    
    return render(request,'analyze.html',params)
    