from django.shortcuts import render
from django.http import HttpResponse
from . import data_process

def index(request):
    # This runs every time the index page is hit, so it incresases the counts, should only be called once.
    data_process.count_legislator_votes()
    data_process.count_bill_votes()
    http_response_text = f"*** Votes information: \n\n LEGISLATOR COUNT: \n{data_process.legislator_vote_count} \n\n BILLS COUNT: \n {data_process.bill_vote_count}"
    return HttpResponse(http_response_text)

def votes(request):
    # TODO: replace data_process methods by API endpoint for data access
    data_results = {}
    data_results["legislator_votes"] = data_process.legislator_vote_count.values()
    data_results["bill_votes"] = data_process.bill_vote_count.values()
    return render(request, 'votes.html',  {'legislators': data_results["legislator_votes"], 'bills': data_results["bill_votes"]})
