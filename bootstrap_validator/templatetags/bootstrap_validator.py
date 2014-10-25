# coding=utf-8
import json
from django import template
from django.contrib.staticfiles import utils
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.forms.forms import BoundField

register = template.Library()


def _get_static_url(path):
    from django.contrib.staticfiles.storage import staticfiles_storage

    return staticfiles_storage.url(path)


@register.simple_tag
def validator_javascript_url():
    return _get_static_url('js/bootstrapValidator.min.js')


@register.simple_tag
def validator_css_url():
    return _get_static_url('css/bootstrapValidator.min.css')


@register.simple_tag
def validator(selector, form, *args, **kwargs):
    container = kwargs.pop('container', 'tooltip')
    icon = kwargs.pop('icon', None)
    validators = {}
    for field in form:
        validators[field.name] = render_field(field)
    code = (u"$(document).ready(function() {{ \r\n"
            u"      $('{selector}').bootstrapValidator({{  \r\n"
            u"          container:'{container}',  \r\n"
            u"          message: 'This value is not valid',  \r\n"
            u"          feedbackIcons: {icon},  \r\n"
            u"          fields:{fields} \r\n"
            u"      }}) \r\n"
            u'  }});')
    icon = icon.lower() if icon else None
    if icon == 'bootstrap' or icon == "buildin":
        icon_code = (u"{ \r\n"
                     u"valid: 'glyphicon glyphicon-ok', \r\n"
                     u"invalid: 'glyphicon glyphicon-remove', \r\n"
                     u"validating: 'glyphicon glyphicon-refresh' \r\n"
                     u"} \r\n")
    elif icon == 'fa' or icon == 'fontawesome':
        icon_code = (u" { \r\n"
                     u"valid: 'fa fa-check', \r\n"
                     u"invalid: 'fa fa-times', \r\n"
                     u"validating: 'fa fa-refresh' \r\n"
                     u"} \r\n")
    else:
        icon_code = 'null'
    return code.format(selector=selector, container=container, icon=icon_code, fields=json.dumps(validators, indent=4))


def render_field(field):
    """
    渲染字段验证代码
    :param field:
     :type field: django.forms.Field
    :return:
    """
    field = field.field if isinstance(field, BoundField) else field
    validators = {}
    if field.required:
        validators['notEmpty'] = {'message': "This field is required."}
    for v in field.validators:
        if isinstance(v, MinLengthValidator):
            vc = validators.get('stringLength', {})
            vc['min'] = field.min_length
            validators.update({'stringLength': vc})
        elif isinstance(v, MaxLengthValidator):
            vc['max'] = field.max_length
            validators.update({'stringLength': vc})
        elif isinstance(v, MinValueValidator):
            vc = validators.get('between', {})
            vc['min'] = field.min_value
            validators.update({'between': vc})
        elif isinstance(v, MaxValueValidator):
            vc['max'] = field.max_value
            validators.update({'between': vc})
    return {'validators': validators}