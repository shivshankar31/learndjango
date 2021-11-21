from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# now with below function integers also handled 

def monthly_challenge_as_int(request, month):
    return HttpResponse(month)


def monthly_challenges(request, month):
    if month == 'january':
        return HttpResponse('This in january, Always dream your dream!') 
    elif month == 'february':
        return HttpResponse('This is february, Work smart and earn better!')
    elif month == 'march':
        return HttpResponse('This is march, Run with the phase, do not stop when you fail!')
    else:
        return HttpResponseNotFound('This month is not included')
    
# it can be return using a variable as well, 
# def monthly_challenges(request, month):
#     challenge_text = None
#     if month == 'january':
#         challenge_text = 'This in january, Always dream your dream!' 
#     elif month == 'february':
#         challenge_text = 'This is february, Work smart and earn better!' #this text can be given inside a tupple as well see below 
#     elif month == 'march':
#         challenge_text = ('This is march, Run with the phase, do not stop when you fail!')
#     else:
#         return HttpResponseNotFound('This month is not included')
    
#     return HttpResponse(challenge_text)
