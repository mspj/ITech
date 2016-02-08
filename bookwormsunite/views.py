from django.http import HttpResponse


def index(request):
    html = "<html><body>index</body></html>"
    return HttpResponse(html)


def readathon_info(request, readathon_name_slug):
    html = "<html><body>readathon_info: {0}</body></html>".format(readathon_name_slug)
    return HttpResponse(html)


def user_info(request, uid):
    html = "<html><body>user_info: {0}</body></html>".format(uid)
    return HttpResponse(html)


def user_summary(request, uid):
    html = "<html><body>user_summary: {0}</body></html>".format(uid)
    return HttpResponse(html)


def login(request):
    if request.method != "POST":
        return HttpResponse('Method not allowed', status=405)
    html = "<html><body>login</body></html>"
    return HttpResponse(html)


def register(request):
    if request.method != "POST":
        return HttpResponse('Method not allowed', status=405)
    html = "<html><body>register</body></html>"
    return HttpResponse(html)


def search(request):
    if request.method != "POST":
        return HttpResponse('Method not allowed', status=405)
    html = "<html><body>search</body></html>"
    return HttpResponse(html)
