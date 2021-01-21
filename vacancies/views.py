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
        vacancies = Vacancy.objects.filter(specialty=specialty_code).all()
        specialty = Specialty.objects.filter(code=specialty_code)
        count = vacancies.count()
        word = vacancy_declension(count)
    else:
        vacancies = Vacancy.objects.all()
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


def companies_view(request, company_id=None):
    return render(request, 'company.html')


def vacancy_view(request, job_id):
    return render(request, 'vacancy.html')


def vacancy_declension(num):
    n = int(str(num)[-1])
    m = int(str(num // 10)[-1])
    if n == 1 and m != 1:
        return 'вакансия'
    elif 1 < n < 5 and m != 1:
        return 'вакансии'
    else:
        return 'вакансий'
