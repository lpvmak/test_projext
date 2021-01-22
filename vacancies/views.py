from django.db.models import Count
from django.shortcuts import render

from vacancies.models import Specialty, Company, Vacancy


def main_view(request):
    specialties = Specialty.objects.annotate(num_vacancy=Count('vacancies')).all()
    for specialty in specialties:
        specialty.word = vacancy_declension(specialty.num_vacancy)
    companies = Company.objects.annotate(num_vacancy=Count('vacancies')).all()
    for company in companies:
        company.word = vacancy_declension(company.num_vacancy)
    return render(request, 'index.html', {
        'specialties': specialties,
        'companies': companies
    })


def jobs_views(request, specialty_code=None):
    if specialty_code:
        vacancies = Vacancy.objects.filter(specialty__code=specialty_code).all()
        for vacancy in vacancies:
            vacancy.skills_list = vacancy.skills.split(', ')
        specialty = Specialty.objects.filter(code=specialty_code).first()
        count = vacancies.count()
        word = vacancy_declension(count)
    else:
        vacancies = Vacancy.objects.all()
        for vacancy in vacancies:
            vacancy.skills_list = vacancy.skills.split(', ')
        specialty = None
        count = vacancies.count()
        word = vacancy_declension(count)
    return render(request, 'vacancies.html', {
        'vacancies': vacancies,
        'specialty_code': specialty_code,
        'specialty': specialty,
        'count': count,
        'word': word
    })


def company_view(request, company_id):
    company = Company.objects.filter(id=company_id).first()
    vacancies = Vacancy.objects.filter(company__id=company_id).all()
    for vacancy in vacancies:
        vacancy.skills_list = vacancy.skills.split(', ')
    count = vacancies.count()
    word = vacancy_declension(count)
    return render(request, 'company.html', {
        'company': company,
        'vacancies': vacancies,
        'count': count,
        'word': word
    })


def vacancy_view(request, job_id):
    vacancy = Vacancy.objects.filter(id=job_id).first()
    vacancy.skills_list = vacancy.skills.split(', ')
    return render(request, 'vacancy.html', {'vacancy': vacancy})


def vacancy_declension(num):
    n = int(str(num)[-1])
    m = int(str(num // 10)[-1])
    if n == 1 and m != 1:
        return 'вакансия'
    elif 1 < n < 5 and m != 1:
        return 'вакансии'
    else:
        return 'вакансий'
