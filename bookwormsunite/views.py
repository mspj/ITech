import json

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.http import require_http_methods, require_GET, require_POST

from ITech.settings import LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL, SUCCESS_STATUS, FAIL_STATUS, INCORRECT_CREDS_MSG, \
    DISABLED_ACC_MSG, SUCCESS_LOGIN_MSG, SUCCESS_REGISTER_MSG
from bookwormsunite.forms import ReaderCreationForm, PictureForm
from bookwormsunite.models import Readathon, Accomplishment, Reader, Challenge, Activity
from bookwormsunite.utils.api_wrapper import APIWrapper


@require_GET
def index(request):
    title = "Index"
    upcoming_readathons = Readathon.objects.filter(end_date__gt=timezone.now())[:4]
    accomplishments = Accomplishment.objects.order_by('-created')
    recent_books = []
    for accomplishment in accomplishments:
        for book in accomplishment.books.all():
            recent_books.append(book)

    recent_books = list(set(recent_books))[:12]

    today = timezone.now()
    monday = today - timezone.timedelta(days=today.weekday())
    calendar_obj = [{}, {}, {}, {}, {}, {}, {}]

    for i in range(7):
        event_day = monday + timezone.timedelta(i)
        calendar_obj[i]['day'] = event_day
        readathons = Readathon.objects.filter(start_date__lt=event_day, end_date__gt=event_day)
        calendar_obj[i]['readathons'] = readathons

    context_dict = {'title': title, 'upcoming_readathons': upcoming_readathons, 'recent_books': recent_books,
                    'calendar_obj': calendar_obj, 'today': today}
    return render(request, 'bookwormsunite/index.html', context_dict)


@require_POST
def readathon_join(request, readathon_name_slug):
    response = {'status': FAIL_STATUS}
    try:
        readathon = Readathon.objects.get(slug=readathon_name_slug)
        readathon.readers.add(request.user.id)
        response['status'] = SUCCESS_STATUS
        Activity.objects.joined_readathon(request.user, readathon)
    except Readathon.DoesNotExist as e:
        response['msg'] = 'Readathon not found: {0}'.format(e.message)

    return JsonResponse(response)


@require_http_methods(["GET", "POST"])
def readathon_info(request, readathon_name_slug):
    try:
        readathon = Readathon.objects.get(slug=readathon_name_slug)
    except Readathon.DoesNotExist:
        raise Http404('Readathon does not exist')

    challenges = Challenge.objects.filter(readathon=readathon.id).all()

    readers = readathon.readers.all()
    is_joined = False
    if request.user.is_authenticated():
        if len(readers.filter(id=request.user.id)) != 0:
            is_joined = True

    num_books_read = 0
    challenge_books_read = {}
    # This nested for loop can lead to the end of humanity
    # TODO - somebody please make it better
    for challenge in challenges:

        challenge_books_read[challenge.id] = {}
        accomplishments = Accomplishment.objects.filter(challenge=challenge.id)

        dummy_books_read = {}
        is_completed = False
        for accomplishment in accomplishments:
            num_books_read = num_books_read + len(accomplishment.books.all())

            if is_joined and accomplishment.user_id == request.user.id:
                is_completed = True

            for book in accomplishment.books.all():
                if dummy_books_read.get(book) == None:
                    dummy_books_read[book] = [1, False]
                else:
                    dummy_books_read[book][0] = dummy_books_read.get(book)[0] + 1

                if accomplishment.user_id == request.user.id:
                    dummy_books_read[book][1] = is_joined

        challenge_books_read[challenge.id]['is_completed'] = is_completed
        sorted_books_read = sorted(dummy_books_read.items(), key=lambda x: x[1][0], reverse=True)

        challenge_books_read[challenge.id]['details'] = []
        for book, detail in sorted_books_read:
            challenge_books_read[challenge.id]['details'].append((book, detail[0], detail[1]))

    avg_num_books_read = 0
    if len(readers) > 0:
        avg_num_books_read = num_books_read // len(readers)

    title = readathon.name

    is_finished = (readathon.end_date < timezone.now())
    is_started = (readathon.start_date < timezone.now())

    context_dict = {'title': title, 'readathon': readathon, 'challenges': challenges, 'readers': readers,
                    'num_books_read': num_books_read, 'challenge_books_read': challenge_books_read,
                    'avg_num_books_read': avg_num_books_read, 'is_finished': is_finished, 'is_started': is_started,
                    'is_joined': is_joined}
    return render(request, 'bookwormsunite/readathon.html', context_dict)


@require_GET
def user_info(request, uid):
    picture_form = PictureForm()

    joined_readathons = Readathon.objects.filter(readers=uid).order_by('-created')
    try:
        reader = Reader.objects.get(id=uid)
    except Reader.DoesNotExist as e:
        raise Http404('Reader does not exist: {0}'.format(e.message))
    title = reader.username
    activities = Activity.objects.filter(user=uid).order_by('-created')[:10]
    accomplishments = Accomplishment.objects.filter(user_id=uid).order_by('-created')
    recent_books = []
    for accomplishment in accomplishments:
        for book in accomplishment.books.all():
            recent_books.append(book)
    recent_books = list(set(recent_books))[:12]

    context_dict = {'title': title, 'joined_r': joined_readathons, 'reader': reader, 'activities': activities,
                    'accomplishments': accomplishments, 'recent_books': recent_books, 'picture_form': picture_form}
    return render(request, 'bookwormsunite/user_info.html', context_dict)


@require_GET
def user_summary(request, uid):
    title = "Index"
    content = "This is index page"
    context_dict = {'title': title, 'content': content}
    return render(request, 'bookwormsunite/user_summary.html', context_dict)


@require_POST
def login(request):
    response = {'status': FAIL_STATUS}
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)

    if user:
        if user.is_active:
            auth_login(request, user)
            response['status'] = SUCCESS_STATUS
            response['msg'] = SUCCESS_LOGIN_MSG
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
    response = {'status': FAIL_STATUS}
    reader_form = ReaderCreationForm(data=request.POST)
    if reader_form.is_valid():
        reader = reader_form.save(commit=True)
        reader = authenticate(username=reader_form.cleaned_data['username'],
                              password=reader_form.cleaned_data['password'])
        auth_login(request, reader)
        Activity.objects.joined(reader)
        response['status'] = SUCCESS_STATUS
        response['msg'] = SUCCESS_REGISTER_MSG
        response['redirect_to'] = LOGIN_REDIRECT_URL
    else:
        response['msg'] = reader_form.errors
    return JsonResponse(response)


@require_GET
def autocomplete_search(request):
    response = {'status': FAIL_STATUS}
    if request.is_ajax():
        q = request.GET.get('term')
        readathons = Readathon.objects.filter(name__icontains=q)
        results = []
        for readathon in readathons:
            readathon_json = {'label': readathon.name, 'slug': readathon.slug}
            results.append(readathon_json)
        response['result'] = results
        response['status'] = SUCCESS_STATUS
    else:
        response['status'] = FAIL_STATUS
    return JsonResponse(response)


@require_GET
def calendar(request, offset):
    offset = int(offset)

    today = timezone.now()
    monday = today - timezone.timedelta(days=today.weekday())

    if offset < 0:
        monday = monday - timezone.timedelta(abs(offset) * 7)
    else:
        monday = monday + timezone.timedelta(abs(offset) * 7)

    midweek = monday + timezone.timedelta(3)

    calendar_obj = [{}, {}, {}, {}, {}, {}, {}]

    for i in range(7):
        event_day = monday + timezone.timedelta(i)
        calendar_obj[i]['day'] = event_day.strftime("%d")
        readathons = Readathon.objects.filter(start_date__lt=event_day, end_date__gt=event_day)
        calendar_obj[i]['readathons'] = []
        for readathon in readathons:
            calendar_obj[i]['readathons'].append({'name': readathon.name, 'slug': readathon.slug})

    response = {'month': midweek.strftime("%B %Y"), 'calendar_obj': calendar_obj}
    response = json.dumps(response)
    return HttpResponse(response, content_type='application/json')


@require_POST
def upload_pic(request):
    response = {'status': FAIL_STATUS}
    picture_form = PictureForm(request.POST, request.FILES, instance=request.user)

    if picture_form.is_valid():
        user = picture_form.save()
        response['status'] = SUCCESS_STATUS
    else:
        response['msg'] = picture_form.errors

    return JsonResponse(response)


@require_GET
def search_book(request, query):
    response = {'status': FAIL_STATUS}

    apiWrapper = APIWrapper()
    # HTTP Errors are caught in the API Wrapper
    # In case of error, its return None
    res = apiWrapper.search_book(query)
    if res is not None:
        response['status'] = SUCCESS_STATUS
        response['data'] = res
    else:
        response['msg'] = 'Request to Goodreads API failed'
    return JsonResponse(response)


@require_POST
def save_accomplishment(request):
    print 'a'
    # check book
    # Book.objects.filter(isbn=)

    # save book

    # save accomplishent
