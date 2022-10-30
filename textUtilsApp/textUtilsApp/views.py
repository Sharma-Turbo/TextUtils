
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def analyze(request):
   
    djtext=request.POST.get('text','default')
    remove_puc=request.POST.get('puncremove','off')
    uppercase=request.POST.get('uppercase','off')
    lowercase=request.POST.get('lowercase','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    if (remove_puc=='on'):
        punctuations='''~`!@#$%^&*()_|\}{[]}"':;<>?/.,'''
        analyzed=''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        
        params={
                'purpose':'Remove punctuations',
                'analyze_text':analyzed
            }
        djtext=analyzed

    if(uppercase=='on'):
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={
                'purpose':'UPPER CASE',
                'analyze_text':analyzed
            }
        djtext=analyzed


      
   
    if(lowercase=='on'):
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.lower()
        params={
                'purpose':'lower case',
                'analyze_text':analyzed
            }
        djtext=analyzed


      

    if(newlineremover=='on'):
        analyzed=''
        for char in djtext:
            if char != '\n' and char !='\r':
                analyzed=analyzed+char
            else:
                print('no')
        params={
                'purpose':'remove new line',
                'analyze_text':analyzed
            }
        djtext=analyzed
       

    if(extraspaceremover=='on'):
        analyzed=''
        for ind ,char in enumerate(djtext):
            if not(djtext[ind]==' ' and djtext[ind+1]==' '):
                analyzed=analyzed+char

        params={
                'purpose':'remove extra space',
                'analyze_text':analyzed
            }

    if(remove_puc!='on' and extraspaceremover!='on' and newlineremover!='on' and lowercase!='on' and uppercase!='on'):
        return HttpResponse('please select any operations')

    return render(request,'analyze.html',params)
       


    