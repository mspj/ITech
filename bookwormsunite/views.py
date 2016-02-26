from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.http import require_http_methods, require_GET, require_POST

from ITech.settings import LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL, SUCCESS_MSG, FAIL_MSG, INCORRECT_CREDS_MSG, \
    DISABLED_ACC_MSG
from bookwormsunite.forms import ReaderCreationForm
from bookwormsunite.models import Readathon, Book, Accomplishment, Reader, Challenge, Activity, TimeStampedModel


@require_GET
def index(request):
    title = "Index"
    upcoming_readathons = Readathon.objects.filter(start_date__gt=timezone.now())[:4]
    accomplishments = Accomplishment.objects.order_by('-created')
    recent_books = []
    for accomplishment in accomplishments:
        for book in accomplishment.books.all():
            recent_books.append(book)

    recent_books = list(set(recent_books))[:12]

    context_dict = {'title': title, 'upcoming_readathons': upcoming_readathons, 'recent_books': recent_books}
    return render(request, 'bookwormsunite/index.html', context_dict)


@require_http_methods(["GET", "POST"])
def readathon_info(request, readathon_name_slug):
    title = Readathon.objects.get(slug=readathon_name_slug)
    content = Readathon.objects.filter(slug=readathon_name_slug)
    user_in_readathon = Readathon.readers.get()
    challenge = Challenge.objects.filter(slug=readathon_name_slug)
    context_dict = {'title': title, 'content': content, 'challenge':challenge, 'user':user_in_readathon}
    return render(request, 'bookwormsunite/readathon.html', context_dict)


@require_GET
def user_info(request, uid):
    title = "User Information"
    joined_readathons = Readathon.objects.filter(readers=uid)
    reader = Reader.objects.get(id=uid)
    activity = Activity.objects.order_by('-time')[:10]
    context_dict = {'title': title, 'joined_r': joined_readathons, 'reader': reader, 'activity':activity}
    return render(request, 'bookwormsunite/user_info.html', context_dict)


@require_GET
def user_summary(request, uid):
    title = "Index"
    content = "This is index page"
    context_dict = {'title': title, 'content': content}
    return render(request, 'bookwormsunite/user_summary.html', context_dict)


@require_POST
def login(request):
    response = {'status': FAIL_MSG}
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)

    if user:
        if user.is_active:
            auth_login(request, user)
            response['status'] = SUCCESS_MSG
            response['redirect_to'] = LOGIN_REDIRECT_URL
        else:
            response = {'msg': DISABLED_ACC_MSG}
    else:
            response = {'msg': INCORRECT_CREDS_MSG}
    return JsonResponse(response)


@require_GET
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(LOGOUT_REDIRECT_URL)


@require_POST
def register(request):
    response = {'status': FAIL_MSG}
    reader_form = ReaderCreationForm(data=request.POST)
    if reader_form.is_valid():
        reader = reader_form.save(commit=True)
        response['status'] = SUCCESS_MSG
        response['redirect_to'] = LOGIN_REDIRECT_URL
    else:
        response['msg'] = reader_form.errors
    return JsonResponse(response)


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


