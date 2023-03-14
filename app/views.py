from django.shortcuts import render
def condition(request):
    d={'name':123,"age":21,'madhu':145}
    return render(request,'condition.html',d)

# Create your views here.
