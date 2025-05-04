from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Correspondence
from accounts.models import UserDepartment
from .forms import CorrespondenceForm

def get_user_departments(request):
    """ Получаем отделы текущего пользователя """

    user_departments = UserDepartment.objects.filter(user=request.user)  
    departments_to_filter = []
    for user_departments_data in user_departments:
        departments_to_filter.append(str(user_departments_data.department))
    return departments_to_filter

def check_is_user_admin(request):
    """ Проверяем, является ли пользователь админом """

    user_object = User.objects.get(username=request.user)
    if user_object.is_staff == True or user_object.is_superuser == True:
        return True
    else:
        return False

@login_required(login_url="/accounts/login?")
def home(request):
    """ Домашняя страница - список последних 10 писем (по дате). Фильтруем по отделу пользователя (если админ - выводим все). """

    departments_to_filter = get_user_departments(request)
    if check_is_user_admin(request):
        correspondences = Correspondence.objects.all().order_by('-date')[:10]
    else:
        correspondences = Correspondence.objects.filter(department__in=departments_to_filter).order_by('-date')[:10] 
    return render(request,'correspondence_list/correspondence_list.html', {'correspondences':correspondences})

def get_correpnondence_by_access(request, slug):
    """ Получаем письмо из БД, если пользователь - админ, либо если состоит в соответствующем отделе. """

    departments_to_filter = get_user_departments(request)
    try:
        if check_is_user_admin(request):
            correspondence = Correspondence.objects.get(slug=slug)
        else:
            correspondence = Correspondence.objects.filter(slug=slug, department__in=departments_to_filter).get()
        return correspondence
    except ObjectDoesNotExist:
        return HttpResponse(f'Ошибка. Письмо не существует либо отсутствуют необходимые права.')

@login_required(login_url="/accounts/login?")
def correspondence_detail(request, slug):
    """ Детальное отображение письма. """

    correspondence = get_correpnondence_by_access(request, slug)
    return render(request,'correspondence_list/correspondence_detail.html', {'correspondence':correspondence})



@login_required(login_url="/accounts/login?")    
def update_correspondence(request, slug):
    """ Обновляем данные письма и сохраняем в БД. """

    correspondence = get_correpnondence_by_access(request, slug)
    
    if request.method == 'POST':        
        form = CorrespondenceForm(request.POST, request.FILES, instance=correspondence)
        if form.is_valid():
            form.save()          
            return render(request,'correspondence_list/correspondence_detail.html', {'correspondence':correspondence})
    else:
        form = CorrespondenceForm(instance=correspondence)
        
    return render(request,'correspondence_list/correspondence_detail_update.html', {'form': form})

@login_required(login_url="/accounts/login?")
def create_correspondence(request):
    if request.method == 'POST':
        form = CorrespondenceForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('correspondence_list:home')
    else:
        form = CorrespondenceForm()
    return render(request,'correspondence_list/correspondence_create.html', {'form':form})
