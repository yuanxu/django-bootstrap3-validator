# coding=utf-8
import json

from django import template
from django.conf import settings
from django.forms import forms
from django.forms import fields
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.utils.safestring import mark_safe

from ..validators import *
from .utils import convert_datetime_python_to_javascript


register = template.Library()


def _get_static_url(path):
    from django.contrib.staticfiles.storage import staticfiles_storage

    return staticfiles_storage.url(path)


@register.simple_tag
def validator_javascript_url():
    return _get_static_url('validator/js/bootstrapValidator.min.js')


@register.simple_tag
def validator_css_url():
    return _get_static_url('validator/css/bootstrapValidator.min.css')


@register.simple_tag
def validator(selector, form, requirejs=False, *args, **kwargs):
    """

    :param selector:
    :type selector: str
    :param form:
     :type form: django.forms.Form
    :param requirejs:
    :param args:
    :param kwargs:(language,config_requirejs)
    :return:
    """
    if not selector.startswith(u'.') and not selector.startswith('#'):
        selector = '#' + selector
    container = kwargs.pop('container', '')
    icon = kwargs.pop('icon', None)

    validators = {}
    for field in form:
        validators[field.name] = render_field(field)
    code = (u"$(document).ready(function() {{ \r\n"
            u"      $('{selector}').bootstrapValidator({{  \r\n"
            u"          container:'{container}',  \r\n"
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
    elif icon == 'bootstrap2':
        icon_code = (u" { \r\n"
                     u"valid: 'icon-ok', \r\n"
                     u"invalid: 'icon-remove', \r\n"
                     u"validating: 'icon-refresh icon-spin' \r\n"
                     u"} \r\n")
    elif icon:
        icon_code = icon
    else:
        icon_code = 'null'
    vld_code = code.format(selector=selector, container=container, icon=icon_code,
                           fields=json.dumps(validators, indent=4))
    if requirejs:
        depends = '"jquery","bootstrapValidator"'
        if 'language' in kwargs:
            depends = '{},"bootstrapValidator/language/{}"'.format(depends, kwargs['language'])
        vld_code = u'requirejs([{}],function(){{ {} }})'.format(depends, vld_code)

    return mark_safe(vld_code)


@register.simple_tag
def validator_fields(form):
    validators = {}
    for field in form:
        validators[field.name] = render_field(field)
    return mark_safe(json.dumps(validators, indent=4))


@register.simple_tag
def validator_requirejs_config(base_url=None, language=None):
    config = ("requirejs.config({{"
              "paths:{{"
              "'bootstrapValidator':'{bv}/bootstrapValidator.min',"
              "'bootstrapValidator/language/{lang}':'{bv}/language/{lang}',"
              "}},"
              "shim:{{"
              "'bootstrapValidator':['jquery'],"
              "'bootstrapValidator/language/{lang}':['bootstrapValidator']"
              "}}"
              "}});")
    if base_url is None:
        bv = getattr(settings, 'BOOTSTRAP_VALIDATOR_PREFIX', '')
        if not bv:
            bv = _get_static_url('validator/js')
    else:
        bv = base_url
    if bv.endswith("/"):
        bv = bv[:-1]
    language = language if language else ''

    return mark_safe(config.format(bv=bv, lang=language))


def render_field(field):
    """
    渲染字段验证代码
    :param field:
     :type field: django.forms.Field
    :return:
    """
    field = field.field if isinstance(field, forms.BoundField) else field
    validators = {}

    def no_compare_validator():
        return not ('lessThan' in validators or 'greaterThan' in validators or 'between' in validators)

    if field.required:
        validators['notEmpty'] = {}
    validator_codes = [item.code for item in field.validators]
    for v in field.validators:
        if isinstance(v, MinLengthValidator):
            vc = validators.get('stringLength', {})
            vc['min'] = field.min_length
            validators.update({'stringLength': vc})
        elif isinstance(v, MaxLengthValidator):
            vc = validators.get('stringLength', {})
            vc['max'] = field.max_length
            validators.update({'stringLength': vc})
        elif isinstance(v, (MinValueValidator, MaxValueValidator)):
            if 'min_value' in validator_codes and 'max_value' in validator_codes:
                vc = validators.get('between', {})
                if v.code == 'min_value':
                    vc['min'] = field.min_value
                else:
                    vc['max'] = field.max_value
                validators.update({'between': vc})
            elif v.code == 'min_value':
                validators['greaterThan'] = {'value': field.min_value}
            elif v.code == 'max_value':
                validators['lessThan'] = {'value': field.max_value}
        elif isinstance(v, BaseBV):
            validators.update(v.get_validator_code())

    if isinstance(field, (fields.DecimalField, fields.FloatField)) and no_compare_validator():
        validators['numeric'] = {}
    elif isinstance(field, fields.IntegerField) and no_compare_validator():
        validators['integer'] = {}
    elif isinstance(field, (fields.DateField, fields.DateTimeField)):
        formats = field.input_formats
        if formats:
            validators['date'] = {'format': convert_datetime_python_to_javascript(formats[0])}
    elif isinstance(field, fields.TimeField):
        validators['regexp'] = {'regexp': '^((([0-1]?[0-9])|([2][0-3])):)(([0-5][0-9]):)([0-5][0-9])$',
        }
    elif isinstance(field, fields.URLField):
        validators['uri'] = {}
    elif isinstance(field, fields.EmailField):
        validators['emailAddress'] = {}
    elif isinstance(field, fields.ImageField):
        if 'file' not in validators:
            validators.update(ImageFileValidator().get_validator_code())
    return {'validators': validators}