from django.shortcuts import render

# Create your views here.

def initial_view(request):
    return render(request, 'index.html', {'data': [1,2,3,4,5]})
