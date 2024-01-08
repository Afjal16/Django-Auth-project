from django.shortcuts import render
from app1.models import form1
from django.contrib import messages


# from django.db.models import Q

# def search(request):
#     query=request.POST.get('search','')
#     if query:
#         queryset=(Q(title__icontains=query)) | (Q(details__icontains=query)) | 
#         (Q(medium__icontains=query)) | (Q(subject__icontains=query))
#         results=form1.objects.filter(queryset).distinct()
#     else:
#         results=[]
        
#         context={
#             'results':results
#         }
#         return render(request,"search.html",context)

# Create your views here.
def INDEX(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        details=form1(name=name, email=email)
        details.save()
        messages.success(request, "Successfully")
    return render(request, 'index.html')

