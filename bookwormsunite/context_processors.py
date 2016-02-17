from bookwormsunite.forms import ReaderForm, ReaderCreationForm


def include_login_form(request):
    reader_form = ReaderForm()
    return {'login_form': reader_form}


def include_register_form(request):
    register_form = ReaderCreationForm()
    return {'register_form': register_form}
