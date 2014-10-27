# coding=utf-8
from warnings import warn
from django.shortcuts import resolve_url


class BaseBV(object):
    code = ''

    def __call__(self, value):
        # value = force_text(value)
        # TODO: support server side validation
        warn("Bootstrap_Validator.%s not support server side validation now." % self.code)
        return

    def get_validator_code(self):
        return {}


class IdValidator(BaseBV):
    """
    Validate identification number
    http://bootstrapvalidator.com/validators/id/
    """
    code = 'id'
    COUNTRIES = {'BA': 'Bosnia and Herzegovina',
                 'BG': 'Bulgaria',
                 'BR': 'Brazil',
                 'CH': 'Switzerland',
                 'CL': 'Chile',
                 'CN': 'China',
                 'CZ': 'Czech Republic',
                 'DK': 'Denmark',
                 'EE': 'Estonia',
                 'ES': 'Spain',
                 'FI': 'Finland',
                 'HR': 'Croatia',
                 'IE': 'Ireland',
                 'IS': 'Iceland',
                 'LT': 'Lithuania',
                 'LV': 'Latvia',
                 'ME': 'Montenegro',
                 'MK': 'Macedonia',
                 'NL': 'Netherlands',
                 'RO': 'Romania',
                 'RS': 'Serbia',
                 'SE': 'Sweden',
                 'SI': 'Slovenia',
                 'SK': 'Slovakia',
                 'SM': 'San Marino',
                 'TH': 'Thailand',
                 'ZA': 'South Africa'}

    def __init__(self, country):
        """

        :param country: 可以是国家代码，或者是另外一个控件名字的引用
        :return:
        """
        self.country = country

    def get_validator_code(self):
        return {self.code: {'country': self.country}}


class ZipCodeValidator(BaseBV):
    """
    :param country: 可以是国家代码，或者是另外一个控件名字的引用
    """
    code = 'zipZode'
    COUNTRIES = {
        'BR': 'Brazil',
        'CA': 'Canada',
        'CZ': 'Czech Republic',
        'DK': 'Denmark',
        'GB': 'United Kingdom',
        'IT': 'Italy',
        'MA': 'Morocco',
        'NL': 'Netherlands',
        'RO': 'Romania',
        'RU': 'Russia',
        'SE': 'Sweden',
        'SG': 'Singapore',
        'SK': 'Slovakia',
        'US': 'USA'
    }

    def __init__(self, country):
        self.country = country

    def __call__(self, value):
        # value = force_text(value)
        # TODO: support server side validation
        warn("Bootstrap_Validator.zipCode not support server side validation now.")
        return

    def get_validator_code(self):
        return {self.code: {'country': self.country}}


class IdenticalValidator(BaseBV):
    """
    Check if the value is the same as one of particular field

    http://bootstrapvalidator.com/validators/identical/
    """
    code = 'identical'

    def __init__(self, field):
        self.field = field

    def get_validator_code(self):
        return {self.code: {'field': self.field}}


class DifferentValidator(object):
    """
    Return true if the input value is different with given field's value

    http://bootstrapvalidator.com/validators/diffenert/
    """
    code = 'different'

    def __init__(self, field):
        self.field = field

    def get_validator_code(self):
        return {self.code: {'field': self.field}}


class RemoteValidator(BaseBV):
    """
    Perform remote checking via Ajax request

    http://bootstrapvalidator.com/validators/remote/
    """

    code = 'remote'

    def __init__(self, url, type='GET', name=None, data=None, delay=None):
        self.url = url
        self.type = type
        self.name = name
        self.data = data
        self.delay = delay

    def get_validator_code(self):
        vc = {'url': resolve_url(self.url),
              'type': self.type}
        if self.name:
            vc['name'] = self.name
        if self.data:
            vc['data'] = self.data
        if self.delay:
            vc['delay'] = self.delay
        return {'remote': vc}


class ChoicesValidator(BaseBV):
    """
    Check if the number of checked boxes are less or more than a given number

    http://bootstrapvalidator.com/validators/choice/
    """
    code = 'choices'

    def __init__(self, _min, _max):
        self.min = _min
        self.max = _max

    def get_validator_code(self):
        return {self.code: {'min': self.min, 'max': self.max}}


class CallBackValidatgor(BaseBV):
    """
    Return the validity from a callback method

    http://bootstrapvalidator.com/validators/callback/
    """
    code = 'callback'

    def __init__(self, callback):
        """

        :param callback: the callback code or function name
        :return:
        """
        self.callback = callback

    def get_validator_code(self):
        return {self.callback: {'callback': self.callback}}


class PhoneValidator(BaseBV):
    """
    Validate a phone number

    http://bootstrapvalidator.com/validators/phone/
    """
    code = 'phone'
    COUNTRIES = {
        'BR': 'Brazil',
        'CN': 'China',
        'CZ': 'Czech Republic',
        'DK': 'Denmark',
        'ES': 'Spain',
        'FR': 'France',
        'GB': 'United Kingdom',
        'MA': 'Morocco',
        'PK': 'Pakistan',
        'RO': 'Romania',
        'RU': 'Russia',
        'SK': 'Slovakia',
        'TH': 'Thailand',
        'US': 'USA',
        'VE': 'Venezuela'
    }

    def __init__(self, country):
        self.country = country

    def get_validator_code(self):
        return {self.code: {'country': self.country}}


class EmailAddressValidator(BaseBV):
    code = 'emailAddress'

    def __init__(self, multiple=False, separator='/[,;]/'):
        self.multiple = multiple
        self.separator = separator

    def get_validator_code(self):
        return {self.code: {'multiple': str(self.multiple).lower(),
                            'separator': self.separator}}


class UriValidator(BaseBV):
    code = 'uri'

    def __init__(self, allowLocal=False, protocol='http,https,ftp'):
        self.allowLocal = allowLocal
        self.protocol = protocol

    def get_validator_code(self):
        return {self.code: {'allowLocal': str(self.allowLocal).lower(),
                            'protocol': self.protocol}}