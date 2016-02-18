from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, View
from django.contrib.auth import login as auth_login, logout as auth_logout

from bookwormsunite.forms import ReaderForm, ReaderCreationForm
from bookwormsunite.models import Readathon
from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from ITech.settings import LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL
import twitter
# from datetime import datetime
# from django.core.cache import cache
from django.conf import settings

@require_GET
def index(request):
    title = "Index"
    content = "This is index page"
    context_dict = {'title': title, 'content': content, 'tweets': get_tweet()}
    return render(request, 'bookwormsunite/index.html', context_dict)


@require_http_methods(["GET", "POST"])
def readathon_info(request, readathon_name_slug):
    title = "Readathon"
    content = "This is readathon page"
    context_dict = {'title': title, 'content': content}
    return render(request, 'bookwormsunite/readathon.html', context_dict)


@require_GET
def user_info(request, uid):
    title = "User Information"
    content = "This is user information page"
    context_dict = {'title': title, 'content': content}
    return render(request, 'bookwormsunite/user_info.html', context_dict)


@require_GET
def user_summary(request, uid):
    title = "Index"
    content = "This is index page"
    context_dict = {'title': title, 'content': content}
    return render(request, 'bookwormsunite/user_summary.html', context_dict)


@require_POST
def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)

    if user:
        if user.is_active:
            auth_login(request, user)
            return HttpResponseRedirect(LOGIN_REDIRECT_URL)
        else:
            return HttpResponse("Your account is disabled.")
    return HttpResponse(status=401)


@require_GET
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(LOGOUT_REDIRECT_URL)


@require_POST
def register(request):
    reader_form = ReaderCreationForm(data=request.POST)
    if reader_form.is_valid():
        reader = reader_form.save(commit=True)
    else:
        return HttpResponse(status=400)
    return HttpResponse(status=200)


@require_POST
def search(request):
    if request.method == "POST":
        search_text = request.POST['query']
    else:
        search_text = ''
    try:
        readathons = Readathon.objects.filter(name__contains=search_text)
    except Readathon.DoesNotExist:
        readathons = None
        pass
    context_dict = {'readathons': readathons}
    return render(request, 'bookwormsunite/base.html', context_dict)

def get_tweet():
    tweets = []
    try:
        api = twitter.Api()
        # print(api.GetUserTimeline(screen_name='@MailOnline'))
        lastest = api.GetUserTimeline(screen_name=set)
        for tweet in lastest:
            status = tweet.text
            print(status)
            tweet_date = tweet.relative_created_at
            tweets.append({'status':status, 'date': tweet_date})
    except:
        tweets.append({'status': 'Follow as ...', 'date': 'about 10 minutes ago'})
    return {'tweets':tweets}