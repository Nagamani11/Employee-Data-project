from django.http import HttpResponse
from django.shortcuts import render
from .models import EmployeeData
from django.db.models import Q
import random
import faker
fake = faker.Faker()
def mainPage(request):
    if request.method == "GET":
        return render(request, 'mainpage.html')

def dataGenerate(request):
    fake.unique.clear()
    for i in range(1000):
        fname1 = fake.first_name()
        lname1 = fake.last_name()
        salary1 = fake.random_int(min=10000, max=100000)
        company1 = fake.random_element(elements=('Infosys','Wipro','HCL','TCS','MNC'))
        email1 = fake.email()
        location1 = fake.random_element(elements=('Hyderabad','Banglore','Chennai','Mumbai','Delhi'))
        home_town1 = fake.random_element(elements=('Guntur','Vijayawada','Jaggayyapeta','Nandigama','suryapeta'))
        qualification1 = fake.random_element(elements=('BTech','MTech','Degree','MCA','MBA'))
        skill1 = fake.random_element(elements=('Python','Java','PHP','Django','Devops'))
        percentage1 = fake.random_int(min=35, max=100)
        EmployeeData(
                    first_name = fname1,
                    last_name = lname1,
                    salary = salary1,
                    company = company1,
                    email = email1,
                    location = location1,
                    home_town = home_town1,
                    qualification = qualification1,
                    skill = skill1,
                    percentage = percentage1,
                ).save()
    return HttpResponse('Data Saved!!!')

def hyderabad(request):
    if request.method == 'GET':
        data = EmployeeData.objects.filter(location='Hyderabad')
        return render(request, 'hyderabad.html', {'data':data})
    else:
        company_search = request.POST.get('company')
        data = EmployeeData.objects.filter(location='Hyderabad')
        if company_search:
            data = data.filter(
            Q(company__icontains=company_search)|
            Q(salary__icontains=company_search)|
            Q(location__icontains=company_search)|
            Q(home_town__icontains=company_search)|
            Q(qualification__icontains=company_search)|
            Q(skill__icontains=company_search)|
            Q(percentage__icontains=company_search)
            )
        return render(request, 'hyderabad.html', {'data':data})


def banglore(request):
    if request.method == 'GET':
        data = EmployeeData.objects.filter(location='Banglore')
        return render(request, 'banglore.html', {'data':data})
    else:
        company_search = request.POST.get('company')
        data = EmployeeData.objects.filter(location='Banglore')
        if company_search:
            data = data.filter(
            Q(company__icontains=company_search)|
            Q(salary__icontains=company_search)|
            Q(location__icontains=company_search)|
            Q(home_town__icontains=company_search)|
            Q(qualification__icontains=company_search)|
            Q(skill__icontains=company_search)|
            Q(percentage__icontains=company_search)
            )
        return render(request, 'banglore.html', {'data':data})



def chennai(request):
    if request.method == 'GET':
        data = EmployeeData.objects.filter(location='Chennai')
        return render(request, 'chennai.html', {'data':data})
    else:
        company_search = request.POST.get('company')
        data = EmployeeData.objects.filter(location='Chennai')
        if company_search:
            data = data.filter(
            Q(company__icontains=company_search)|
            Q(salary__icontains=company_search)|
            Q(location__icontains=company_search)|
            Q(home_town__icontains=company_search)|
            Q(qualification__icontains=company_search)|
            Q(skill__icontains=company_search)|
            Q(percentage__icontains=company_search)
            )
        return render(request, 'chennai.html', {'data':data})


def mumbai(request):
    if request.method == 'GET':
        data = EmployeeData.objects.filter(location='Mumbai')
        return render(request, 'mumbai.html', {'data':data})
    else:
        company_search = request.POST.get('company')
        data = EmployeeData.objects.filter(location='Mumbai')
        if company_search:
            data = data.filter(
            Q(company__icontains=company_search)|
            Q(salary__icontains=company_search)|
            Q(location__icontains=company_search)|
            Q(home_town__icontains=company_search)|
            Q(qualification__icontains=company_search)|
            Q(skill__icontains=company_search)|
            Q(percentage__icontains=company_search)
            )
        return render(request, 'mumbai.html', {'data':data})



def delhi(request):
    if request.method == 'GET':
        data = EmployeeData.objects.filter(location='Delhi')
        return render(request, 'delhi.html', {'data':data})
    else:
        company_search = request.POST.get('company')
        data = EmployeeData.objects.filter(location='Delhi')
        if company_search:
            data = data.filter(
            Q(company__icontains=company_search)|
            Q(salary__icontains=company_search)|
            Q(location__icontains=company_search)|
            Q(home_town__icontains=company_search)|
            Q(qualification__icontains=company_search)|
            Q(skill__icontains=company_search)|
            Q(percentage__icontains=company_search)
            )
        return render(request, 'delhi.html', {'data':data})


def allData(request):
    if request.method == 'GET':
        data = EmployeeData.objects.all()
        return render(request, 'alldata.html',{'data':data})
    else:
        company_search = request.POST.get('company')
        data = EmployeeData.objects.all()
        if company_search:
            data = data.filter(
            Q(company__icontains=company_search)|
            Q(salary__icontains=company_search)|
            Q(location__icontains=company_search)|
            Q(home_town__icontains=company_search)|
            Q(qualification__icontains=company_search)|
            Q(skill__icontains=company_search)|
            Q(percentage__icontains=company_search)
            )
        return render(request, 'alldata.html',{'data':data})
