from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def index(request):
#     return HttpResponse("this is index page")
# def about(request):
#     return HttpResponse("this is about page")
# def careers(request,pageno):
#     print(request.url)
#     return HttpResponse(f"this is careers page {pageno}")


# dict1={'Skill': 'Python', 'Experience' : 3, 'Location': 'Hyderabad'}
# Location ='Pune'

def index(request):
    return render(request, 'demoapp/index.html')
def about(request):
    return render(request, 'demoapp/about.html')

# def careers(request):
#     return render(request, 'demoapp/careers.html', {'dictionary':dict1})

# def careers(request):
#     return render(request, 'demoapp/careers.html', {'price':500})

#25-04

requirements={'Skill': 'Python', 'Experience' : 3, 'Location': 'Hyderabad'}
Req_skills=['Python', 'Django', 'TypeScript', 'React JS']
def careers(request):
    # return render(request, 'demoapp/careers.html', {'job_req':requirements})
    return render(request, 'demoapp/careers.html', {'skill_set':Req_skills})

    
