from django.shortcuts import render
from django.http import HttpResponse
from . import data_process

def index(request):
    http_response_text = f"*** Votes information: \n\n LEGISLATOR COUNT: \n{data_process.legislator_vote_count} \n\n BILLS COUNT: \n {data_process.bill_vote_count}"
    return HttpResponse(http_response_text)

def votes(request):
    # TODO: replace data_process methods by API endpoint for data access
    data_results = {}
    data_results["legislator_votes"] = data_process.legislator_vote_count.values()
    data_results["bill_votes"] = data_process.bill_vote_count.values()
    return render(request, 'votes.html',  {'legislators': data_results["legislator_votes"], 'bills': data_results["bill_votes"]})

def load_data(request):
    return_msg = ""
    # This loads csv data only once, when the dictionaries are still empty {}
    if data_process.legislator_vote_count == {}:
        return_msg = "*** Legislator not processed. Load data from CSV"
        data_process.count_legislator_votes()
    else:
        return_msg = "*** Legislators already loaded. Do nothing."

    if data_process.bill_vote_count == {}:
        data_process.count_bill_votes()
    else:
        return_msg = "*** Bills already loaded. Do nothing."

    loaded_legislators = (data_process.legislator_vote_count.values() is not None)
    loaded_bills = (data_process.bill_vote_count.values() is not None)
    if loaded_legislators and loaded_bills:
        return HttpResponse(f"Legislators and bills loaded successfully. | {return_msg}.")
    return HttpResponse(f"Error! Legislators or bills data were not loaded successfully.  | {return_msg}")
