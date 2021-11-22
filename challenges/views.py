from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string 

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
    'december' : None
    
}

# to create index page containing all month
# creat a empty list and generate all the keys from dict 
# with that using for loop generate list of path 

def index(request):
    # list_item = ''
    months = list(monthly_challenges_text.keys())
    # using render function to call the intex.html file
    return render(request, 'challenges/index.html', {'months': months}) 
    # as we are using seperate index.html file we donot need to generate here so remove below codes

    # for month in months:
    #     cap_month = month.capitalize()
    #     month_path = reverse('challanges_urlpath', args=[month])
    #     list_item += f'<li><a href="{month_path}">{cap_month}</a><li>'

    # respose_data = f'<ul>{list_item}</ul>'
    # return HttpResponse(respose_data)


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
        # instead of capitialize() here we can use django filterto formate inside html file  
        # cap = month.capitalize()
        # 'render' is a second option insted of 'render_to_string', render is imported from django.shortcutes
        # to convert dynamic html page we use third arg with the dict as below, this 'text' name will be added to the html page with django syntax
        return render(request, 'challenges/challenge.html', {'text': challenge_text, 'month': month}) 

        #why we create challenges folder inside templetes, it is to avoide file duplications, its a best pratice to follow
        # html_response = render_to_string('challenges/challenge.html') # this is to call the html file after this we need to register the app with django setting.py file 
    except:
        raise Http404() # this will look for 404 html file so create the file in globel templates folder