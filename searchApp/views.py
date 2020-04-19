import requests
from django.shortcuts import render
from .models import Candidate
from .forms import CandidateForm
from Search.search import *
# Create your views here.

def index(request):

    search = ''
    dict = {}

    if request.method == 'POST':
            search = request.POST.get('search')
            print(search)

    form = CandidateForm()

    if search is not None:
       dict = retrieveCandidate(search)

    # cities = City.objects.all()
    Candidates = dict
    Candidates_data = []

    for candidate in Candidates:

        candiate_info = {
            'name': candidate.email,
            'email': candidate.name,
            'description': candidate.phone,
            'url' : candidate.url,
        }

        Candidates_data.append(candiate_info)

    context = {'Candidates_data' : Candidates_data,'form':form}
    return render(request, 'searchApp/page.html', context)


