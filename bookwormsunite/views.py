from django.http import HttpResponse, Http404
from django.views.decorators.http import require_http_methods
from bookwormsunite.models import Readathon
from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET, require_POST

@require_GET
def index(request):
    title = "Index"
    content = "This is index page"
    context_dict = {'title': title, 'content': content}
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
    html = "<html><body>login</body></html>"
    return HttpResponse(html)


@require_POST
def register(request):
    html = "<html><body>register</body></html>"
    return HttpResponse(html)



@require_POST
def search(request):
    # context_dict = {}
    # try:
    #     readathons = Readathon.objects.filter(name=readathon_name)
    # except Readathon.DoesNotExist:
    #     readathons = None
    #     pass
    # print('Hello')
    # context_dict['readathons'] = readathons
    # html = "<html><body>search: {{s}}</body></html>"
    # return HttpResponse(html)

    if request.method == "POST":
        search_text = request.POST['query']
    else:
        search_text = ''
    print(search_text)
    try:
        readathons = Readathon.objects.filter(name__contains=search_text)
    except Readathon.DoesNotExist:
        readathons = None
        pass

    return render('bookwormsunite/base.html', {'readathons': readathons})
    # if request.method == 'POST':
    #     query = request.POST['query'].strip()
    #     if query:
    #         result_list = run_query(query)
    #         context_dict['result_list'] = result_list
    #
    # # Go render the response and return it to the client.
    # return render_to_response('base.html', context_dict, context)
