from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from main import models
from .import forms
from django.contrib.auth.decorators import login_required
# Create your views here.

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

@login_required(login_url='login')
def home(request):
    painting = models.Painting.objects.count()
    mapping = models.Mapping.objects.count()
    connecting = models.Connecting.objects.count()  
    
    context = {'painting_count': painting, 'mapping_count': mapping, 'connecting_count': connecting}
    return render(request, 'dash/index.html', context)


def logindash(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Szia ' + username + '!')
            return redirect('dash-home')  # Replace 'index' with the appropriate URL name or path
        else:
            messages.info(request, 'Helytelen felhasználónév vagy jelszó')

    # If it's a GET request or authentication fails:
    context = {}
    return render(request, 'dash/login.html', context)

@login_required(login_url='login')
def logoutdash(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def uploadCategoryMapping(request):
    form = forms.MappingCategoryForm()
    if request.POST:
        form = forms.MappingCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The mapping category has been updated!')
            redirect('upload-categories')
        else:
            messages.error(request, 'Something went wrong during the uplaoding process!')
            
    context = {'form': form}
    return render(request, 'dash/upload-category.html', context)

@login_required(login_url='login')
def uploadCategoryConnecting(request):
    form = forms.ConnectingCategoryForm()
    if request.POST:
        form = forms.ConnectingCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The connecting category has been updated!')
            redirect('upload-category')
        else:
            messages.error(request, 'Something went wrong during the uplaoding process!')
            
    context = {'form': form}
    return render(request, 'dash/upload-category.html', context)

@login_required(login_url='login')
def uploadCategoryPainting(request):
    form = forms.PaintingCategoryForm()
    if request.POST:
        form = forms.PaintingCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The painting category has been updated!')
            redirect('upload-category')
        else:
            messages.error(request, 'Something went wrong during the uplaoding process!')
            
    context = {'form': form}
    return render(request, 'dash/upload-category.html', context)

@login_required(login_url='login')
def uploadCategories(request):
    
    return render(request, 'dash/upload-categories.html')

@login_required(login_url='login')
def category(request):
    mapping = models.MappingCategory.objects.all()
    connecting = models.ConnectingCategory.objects.all()
    painting = models.PaintingCategory.objects.all()
    
    context = {'mappings': mapping, 'connectings': connecting, 'paintings': painting,}
    return render(request, 'dash/category.html', context)

@login_required(login_url='login')
def deleteCategoryMapping(request, pk):
    mapping = models.MappingCategory.objects.get(id=pk)
    if request.method == 'POST':
        mapping.delete()
        messages.success(request, 'The object has been deleted!')
        return redirect('category')
    context = {'obj': mapping}
    return render(request, 'dash/delete.html', context)

@login_required(login_url='login')
def deleteCategoryConnecting(request, pk):
    connecting = models.ConnectingCategory.objects.get(id=pk)
    if request.method == 'POST':
        connecting.delete()
        messages.success(request, 'The object has been deleted!')
        return redirect('category')
        
    context = {'obj': connecting}
    return render(request, 'dash/delete.html', context)

@login_required(login_url='login')
def deleteCategoryPainting(request, pk):
    painting = models.PaintingCategory.objects.get(id=pk)
    if request.method == 'POST':
        painting.delete()
        messages.success(request, 'The object has been deleted!')
        return redirect('category')
        
    context = {'obj': painting}
    return render(request, 'dash/delete.html', context)


@login_required(login_url='login')
def uploadPainting(request):
    form = forms.PaintingForm()
    if request.method == 'POST':
        form = forms.PaintingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'The painting has been uploaded')
            return redirect('painting')
        else:
            messages.error(request, 'Something went wrong during the save process!')
    
    context = {'form': form}
    return render(request, 'dash/upload-painting.html', context)

@login_required(login_url='login')
def painting(request):
    paintings = models.Painting.objects.all()
    
    context = {'paintings': paintings}
    return render(request, 'dash/painting.html', context)

@login_required(login_url='login')
def deletePainting(request, pk):
    painting = models.Painting.objects.get(id=pk)
    if request.method == 'POST':
        painting.delete()
        messages.success(request, 'The object has been deleted!')
        return redirect('painting')
        
    context = {'obj': painting}
    return render(request, 'dash/delete.html', context)

@login_required(login_url='login')
def uploadMapping(request):
    form = forms.MappingForm()
    if request.method == 'POST':
        form = forms.MappingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'The mapping has been uploaded')
            return redirect('mapping')
        else:
            messages.error(request, 'Something went wrong during the save process!')
    
    context = {'form': form}
    return render(request, 'dash/upload-mapping.html', context)

@login_required(login_url='login')
def mapping(request):
    mapping = models.Mapping.objects.all()
    
    context = {'mappings': mapping}
    return render(request, 'dash/mapping.html', context)

@login_required(login_url='login')
def deleteMapping(request, pk):
    mapping = models.Mapping.objects.get(id=pk)
    if request.method == 'POST':
        mapping.delete()
        messages.success(request, 'The object has been deleted!')
        return redirect('mapping')
        
    context = {'obj': mapping}
    return render(request, 'dash/delete.html', context)

@login_required(login_url='login')
def uploadConnecting(request):
    form = forms.ConnectingForm()
    if request.method == 'POST':
        form = forms.ConnectingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'The connecing has been uploaded')
            return redirect('connecting')
        else:
            messages.error(request, 'Something went wrong during the save process!')
    
    context = {'form': form}
    return render(request, 'dash/upload-connecting.html', context)

@login_required(login_url='login')
def connecting(request):
    connecting = models.Connecting.objects.all()
    
    context = {'connectings': connecting}
    return render(request, 'dash/connecting.html', context)

@login_required(login_url='login')
def deleteConnecting(request, pk):
    connecting = models.Connecting.objects.get(id=pk)
    if request.method == 'POST':
        connecting.delete()
        messages.success(request, 'The object has been deleted!')
        return redirect('connecting')
        
    context = {'obj': connecting}
    return render(request, 'dash/delete.html', context)


#updates here tomorrow, then call eszter and deploy the project, or i can try some seo (but i dont have any knowledge of that)

@login_required(login_url='login')
def updatePainting(request, pk):
    painting = models.Painting.objects.get(id=pk)
    form = forms.PaintingForm(instance=painting)
    if request.POST:
        form = forms.PaintingForm(request.POST, instance=painting)
        if form.is_valid():
            form.save()
            messages.success(request, 'The painting has been updated!')
            return redirect('painting')
        else:
            messages.error(request, 'Something went wrong during the updating process!')
    
    context = {'form': form}
    return render(request, 'dash/upload-painting.html', context)
        
@login_required(login_url='login')
def updateMapping(request, pk):
    mapping = models.Mapping.objects.get(id=pk)
    form = forms.MappingForm(instance=mapping)
    if request.POST:
        form = forms.MappingForm(request.POST, instance=mapping)
        if form.is_valid():
            form.save()
            messages.success(request, 'The mapping has been updated!')
            return redirect('mapping')
        else:
            messages.error(request, 'Something went wrong during the updating process!')
    
    context = {'form': form}
    return render(request, 'dash/upload-mapping.html', context)

@login_required(login_url='login')
def updateConnecting(request, pk):
    connecting = models.Connecting.objects.get(id=pk)
    form = forms.ConnectingForm(instance=connecting)
    if request.POST:
        form = forms.ConnectingForm(request.POST, instance=connecting)
        if form.is_valid():
            form.save()
            messages.success(request, 'The connecting has been updated!')
            return redirect('connecting')
        else:
            messages.error(request, 'Something went wrong during the updating process!')
    
    context = {'form': form}
    return render(request, 'dash/upload-connecting.html', context)