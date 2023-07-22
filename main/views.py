from django.shortcuts import render, redirect
from .import models
# Create your views here.


def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def home(request):
    painting = models.PaintingCategory.objects.all()
    mapping = models.MappingCategory.objects.all()
    connecting = models.ConnectingCategory.objects.all()
    
    context = {'paintings': painting, 'mappings': mapping, 'connectings': connecting}
    return render(request, 'index.html', context)


def about(request):
    
    context = {}
    return render(request, 'about.html', context)

def cv(request):
    
    context = {}
    return render(request, 'cv.html', context)

def portfolio(request):
    
    context = {}
    return render(request, 'portfolio.html', context)

def info(request):
    
    context = {}
    return render(request, 'info.html', context)


def contact(request):
    
    context = {}
    return render(request, 'contact.html', context)


def connectingTopic(request):
    connecting = models.ConnectingCategory.objects.all()    
    title = 'Connecting'
    
    context = {'title': title, 'category': connecting}
    return render(request, 'connecting-topic.html', context)

def connectingSubTopic(request, pk):
    category = models.ConnectingCategory.objects.get(name=pk)
    connecting = category.connecting_set.all()
    
    context = {'category': category, 'connectings': connecting}
    return render(request, 'connectings.html', context)

def connectingCertain(request, pk):
    connecting = models.Connecting.objects.get(title=pk)
    
    context = {'connecting': connecting}
    return render(request, 'connecting.html', context)

def mappingTopic(request):
    mapping = models.MappingCategory.objects.all()    
    title = 'Mapping'
    
    context = {'title': title, 'category': mapping}
    return render(request, 'mapping-topic.html', context)

def mappingSubTopic(requets, pk):
    category = models.MappingCategory.objects.get(name=pk)
    mapping = category.mapping_set.all()
    
    context = {'category': category, 'mappings': mapping}
    return render(requets, 'mappings.html', context)

def mappingCertain(request, pk):
    mapping = models.Mapping.objects.get(title=pk)
    
    context ={'mapping': mapping}
    return render(request, 'mapping.html', context)

def paintingTopic(request):
    painting = models.PaintingCategory.objects.all()
    title = 'Paintings'
    
    context = {'title': title, 'category': painting}
    return render(request, 'painting-topic.html', context)

def paintingSubTopic(request, pk):
    category = models.PaintingCategory.objects.get(name=pk)
    paintings = category.painting_set.all()
    
    context = {'category': category, 'paintings': paintings}
    return render(request, 'paintings.html', context)

def paintingCertain(request, pk):
    painting = models.Painting.objects.get(name=pk)
    
    context = {'painting': painting}
    return render(request, 'painting.html', context)
    