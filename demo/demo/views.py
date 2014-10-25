from django.views.generic import FormView

from forms import TestForm


class IndexView(FormView):
    form_class = TestForm
    template_name = 'index.html'