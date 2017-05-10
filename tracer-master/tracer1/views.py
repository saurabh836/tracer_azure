from django.contrib.auth.models import User, Group
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tracer1.socialmedia.fb_search import facebook
from tracer1.socialmedia.link_search import Linkedin
from tracer1.socialmedia.twitter_search import get_twitter
from tracer1.socialmedia.pin_search import pinterest, gplus_search, bing_search
from django.http import HttpResponse


fb_api_key = "EAAPEf2NimqgBAA3OvD9BoRkjGFaBgrIYbAIlXZAHTLlfPJfaR9EwZALNR7CYTysTOdYo0SecrpkvEa5D2rB3ZB9yzD0BRpznh63kt16djaN2as3E5ERQZAtQ2H3qYuednNTjswzP6rl40jxkoZBZBDzbW9VZB9CZCOwZD"
id1 = "109554059587193"
fb = facebook(fb_api_key)
ln = Linkedin()
pin = pinterest()



@api_view(['GET', 'POST'])
def facebook_list(request):
    print type(request.POST.get('nam'))
    if request.method == 'GET':
        return HttpResponse(fb.profile_list(request.GET['q']))
    elif request.method == 'POST':
        respo = request.POST.get('nam')
        if respo is None or respo == "":
            print "{" + str(request.POST['nam'])
            Response([])
        else:
            data = fb.profile_list(name=request.POST.get('nam'))
            return HttpResponse(data)


@api_view(['GET', 'POST'])
def linkedIn_list(request):
    print request.POST.get('nam')
    if request.method == 'GET':
        return HttpResponse(ln.link(request.GET['q']))
    elif request.method == 'POST':
        respo = request.POST.get('nam')
        if respo is None or respo == "":
            Response("", status=status.HTTP_400_BAD_REQUEST)
        else:
            data = ln.link(nam=respo)
            return HttpResponse(data)


@api_view(['GET', 'POST'])
def twitter_list(request):
    print request.POST.get('nam')
    if request.method == 'GET':
        return HttpResponse(get_twitter(request.GET['q']))
    elif request.method == 'POST':
        respo = request.POST.get('nam')
        if respo is None or respo == "":
            Response([], status=status.HTTP_400_BAD_REQUEST)
        else:
            data = get_twitter(screen_name=request.POST.get('nam'))
            return HttpResponse(data)


@api_view(['GET', 'POST'])
def all_list(request):
    print request.POST.get('nam')
    if request.method == 'GET':
        twitter = get_twitter("Abhilash Tiwari")
        facebook = fb.profile_list("Abhilash Tiwari")
        linkedin = ln.chk_fun("Abhilash Tiwari")
        data = {"twitter": twitter, "facebook": facebook, "linkedin": linkedin}
        return HttpResponse(data)
    elif request.method == 'POST':
        respo = request.POST.get('nam')
        if respo is None or respo == "":
            Response([], status=status.HTTP_400_BAD_REQUEST)
        else:
            name = request.POST.get('nam')
            twitter = get_twitter(name)
            facebook = fb.profile_list(name)
            linkedin = ln.chk_fun(name)
            data = {"twitter": twitter, "facebook": facebook, "linkedin": linkedin}
            return HttpResponse(data)


@api_view(['GET', 'POST'])
def pinterest_list(request):
    print type(request.POST.get('nam'))
    if request.method == 'GET':
        return HttpResponse(pin.pin_user_search(request.GET['q']))
    elif request.method == 'POST':
        respo = request.POST.get('nam')
        if respo is None or respo == "":
            print "{" + str(request.POST['nam'])
            Response([])
        else:
            data = pin.pin_user_search(nam=request.POST.get('nam'))
            return HttpResponse(data)


@api_view(['GET', 'POST'])
def gplus_list(request):
    print type(request.POST.get('nam'))
    if request.method == 'GET':
        return HttpResponse(gplus_search(request.GET['q']))
    elif request.method == 'POST':
        respo = request.POST.get('nam')
        if respo is None or respo == "":
            print "{" + str(request.POST['nam'])
            Response([])
        else:
            data = gplus_search(nam=request.POST.get('nam'))
            return HttpResponse(data)

        
@api_view(['GET', 'POST'])
def bing_list(request):
    print type(request.POST.get('nam'))
    if request.method == 'GET':
        return HttpResponse(bing_search(request.GET['q']))
    elif request.method == 'POST':
        respo = request.POST.get('nam')
        if respo is None or respo == "":
            print "{" + str(request.POST['nam'])
            Response([])
        else:
            data = bing_search(nam=request.POST.get('nam'))
            return HttpResponse(data)

        
@api_view(['GET', 'POST'])
def welcome(request):
    if request.method == 'GET':
        message = request.GET['q']
        return HttpResponse("<h1>Welcome " + message + "</h1>")
