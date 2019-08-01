from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Landing Page
def index(request): 
    return HttpResponse('This is the Landing Page!')

# Filtered Company search table
def searchTable(request):
    return HttpResponse('The search table Page')

# Company summary page
def summary(request, company_id):
    return HttpResponse(f'Summary page for company {company_id}')
