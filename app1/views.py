from django.shortcuts import render

def homepage(request):
    return render(request, 'app1/homepage.html')
def app1_page(request):
    return render(request, 'app1/sample_page.html')
