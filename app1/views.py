from django.shortcuts import render

def murali(request):
    data='yeraaa'
    d={'name':data}
    return render(request,'murali.html',context=d)
