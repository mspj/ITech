from django.http import HttpResponse
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
    html = "<html><body>search</body></html>"
    return HttpResponse(html)
