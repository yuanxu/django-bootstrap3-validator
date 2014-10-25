# coding=utf-8
import json

from django import template
from django.forms import forms
from django.forms import fields
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator

from .utils import convert_datetime_python_to_javascript


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
    field = field.field if isinstance(field, forms.BoundField) else field
    widget = field.widget
    validators = {}

    def no_compare_validator():
        return not ('lessThan' in validators or 'greaterThan' in validators or 'between' in validators)

    if field.required:
        validators['notEmpty'] = {'message': "This field is required."}
    validator_codes = [item.code for item in field.validators]
    for v in field.validators:
        if isinstance(v, MinLengthValidator):
            vc = validators.get('stringLength', {})
            vc['min'] = field.min_length
            validators.update({'stringLength': vc})
        elif isinstance(v, MaxLengthValidator):
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
        elif isinstance(v, MaxValueValidator):
            validators.update({'between': vc})

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
                                'message': 'Please enter a valid date'}
    return {'validators': validators}