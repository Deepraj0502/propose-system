from django.shortcuts import render

def index(request):
    ans1=ans2=ans3=0
    if(request.POST.get('ans1')!='' or request.POST.get('ans2')!='' or request.POST.get('ans3')!=''):
        if(request.POST.get('ans1')=='techinal coordinator'):
            ans1=1
        if(request.POST.get('ans2')=='pillu'):
            ans2=1
        if(request.POST.get('ans3')=='mummy'):
            ans3=1
    sum=ans1+ans2+ans3
    context={'answers':[ans1,ans2,ans3],'sum':sum}
    return render(request,'index.html',context)
