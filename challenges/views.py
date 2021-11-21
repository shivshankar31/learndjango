from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# 25 adding more dynamic view logic 

# create a dict for all 12 months

monthly_challenges_text = {
    'january' : 'This in january, Always dream your dream!',
    'february' : 'This is february, Work smart and earn better!',
    'march' : 'This is march, Run with the phase, do not stop when you fail!',
    'april' : 'This in april, Always dream your dream!',
    'may' : 'This is may, Work smart and earn better!',
    'june' : 'This is june, Run with the phase, do not stop when you fail!',
    'july' : 'This in july, Always dream your dream!',
    'august' : 'This is august, Work smart and earn better!',
    'september' : 'This is september, Run with the phase, do not stop when you fail!',
    'october' : 'This in october, Always dream your dream!',
    'november' : 'This is november, Work smart and earn better!',
    'december' : 'This is december, Run with the phase, do not stop when you fail!',
    
}

def monthly_challenge_as_int(request, month):
    return HttpResponse(month)

# call created dict with below function and add try block to handle error
    

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_text[month]
    except:
        return HttpResponseNotFound('Type month propery!')
    # return HttpResponseNotFound('This month is not included')
    
    return HttpResponse(challenge_text)
