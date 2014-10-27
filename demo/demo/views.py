from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView

from .forms import TestForm


class IndexView(FormView):
    form_class = TestForm
    template_name = 'index.html'


@csrf_exempt
def remote_valid(request, *args, **kwargs):
    val = request.GET['to_valid']
    if len(val) > 3:
        return HttpResponse("{'valid': true}", content_type='application/json')
    else:
        return HttpResponse("{'valid': false}", content_type='application/json')