from django.shortcuts import render
from .models import BMW

# Create your views here.
def homeview(request):
    context_shop = BMW.objects.all()

    return render(request=request, template_name='index.html', context={'context_shop': context_shop})