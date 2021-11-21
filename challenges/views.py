from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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

# to create index page containing all month
# creat a empty list and generate all the keys from dict 
# with that using for loop generate list of path 

def index(request):
    list_item = ''
    months = list(monthly_challenges_text.keys())

    for month in months:
        cap_month = month.capitalize()
        month_path = reverse('challanges_urlpath', args=[month])
        list_item += f'<li><a href="{month_path}">{cap_month}</a><li>'

    respose_data = f'<ul>{list_item}</ul>'
    return HttpResponse(respose_data)


# reverse() funcion is used to remove hardcode urls to dynamic by specifing name for the path
# incase of changeing path on main url it wont effect the app urls
# in the app url name should be specified for that path()

def monthly_challenge_as_int(request, month):
    if month <= 12:
        months = list(monthly_challenges_text.keys())
        redirecter_month = months[month - 1]
        dynamic_url = reverse('challanges_urlpath', args=[redirecter_month])
        return HttpResponseRedirect(dynamic_url)
    else:
        return HttpResponseNotFound(' Invalid month, enter valid month')

# call created dict with below function and add try block to handle error 
    

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_text[month]
        html_response = f'<h1>{challenge_text}</h1>' #convert into html
    except:
        return HttpResponseNotFound('<h1>Type month propery!<h2>') #convert into html
    # return HttpResponseNotFound('This month is not included')
    
    return HttpResponse(html_response)
