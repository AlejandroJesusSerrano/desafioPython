from django.shortcuts import render
from appfamily.models import Parents
# Create your views here.

def family_list(request):
     parents = Parents.objects.all()
     
     return render(request, "familia.html", {"parents":parents})
