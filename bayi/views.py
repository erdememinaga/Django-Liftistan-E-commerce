from django.shortcuts import render

def bayi_view(request):
    return render(request,'bayi/index.html',{})
