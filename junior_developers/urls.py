"""junior_developers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path

from vacancies.views import main_view, jobs_views, company_view, vacancy_view, custom_handler404, custom_handler500

# Стоило использовать роутинг из задания
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', main_view, name='main'),
    path('vacancies/<str:specialty_code>', jobs_views, name='vacancies'), # /vacancies/cat/<str:specialty_code>
    path('vacancies', jobs_views, name='vacancies_all'),
    path('company/<int:company_id>', company_view, name='company'), # /companies/<int:company_id>
    path('vacancy/<int:job_id>', vacancy_view, name='vacancy'), # /vacancies/<int:job_id>
]

handler404 = custom_handler404
handler500 = custom_handler500
