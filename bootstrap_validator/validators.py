# coding=utf-8
from warnings import warn

from django.utils.encoding import force_text


class BaseBV(object):
    code = ''
    message = None

    def __call__(self, value):
        # value = force_text(value)
        # TODO: support server side validation
        warn("Bootstrap_Validator.%s not support server side validation now." % self.code)
        return

    def get_validator_code(self):
        return {}

    def _patch_message(self, context):
        if self.message:
            context['message'] = self.message
        return context


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

    def __init__(self, country, message=None):
        """

        :param country: 可以是国家代码，或者是另外一个控件名字的引用
        :return:
        """
        self.country = country
        self.message = message

    def get_validator_code(self):
        return {self.code: self._patch_message({'country': self.country})}


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

    def __init__(self, country, message=None):
        self.country = country
        self.message = message

    def __call__(self, value):
        # value = force_text(value)
        # TODO: support server side validation
        warn("Bootstrap_Validator.zipCode not support server side validation now.")
        return

    def get_validator_code(self):
        return {self.code: self._patch_message({'country': self.country})}


class IdenticalValidator(BaseBV):
    """
    Check if the value is the same as one of particular field

    http://bootstrapvalidator.com/validators/identical/
    """
    code = 'identical'

    def __init__(self, field, message=None):
        self.field = field
        self.message = message

    def get_validator_code(self):
        return {self.code: self._patch_message({'field': self.field})}


class DifferentValidator(BaseBV):
    """
    Return true if the input value is different with given field's value

    http://bootstrapvalidator.com/validators/diffenert/
    """
    code = 'different'

    def __init__(self, field, message=None):
        self.field = field
        self.message = message

    def get_validator_code(self):
        return {self.code: self._patch_message({'field': self.field})}


class RemoteValidator(BaseBV):
    """
    Perform remote checking via Ajax request

    http://bootstrapvalidator.com/validators/remote/
    """

    code = 'remote'

    def __init__(self, url, type='GET', name=None, data=None, delay=None, message=None):
        self.url = url
        self.type = type
        self.name = name
        self.data = data
        self.delay = delay
        self.message = message

    def get_validator_code(self):
        vc = {'url': force_text(self.url),  # url maybe lazy,
              'type': self.type}
        if self.name:
            vc['name'] = self.name
        if self.data:
            vc['data'] = self.data
        if self.delay:
            vc['delay'] = self.delay
        else:
            vc['delay'] = 300
        return {'remote': self._patch_message(vc)}


class ChoicesValidator(BaseBV):
    """
    Check if the number of checked boxes are less or more than a given number

    http://bootstrapvalidator.com/validators/choice/
    """
    code = 'choices'

    def __init__(self, _min, _max, message=None):
        self.min = _min
        self.max = _max
        self.message = message

    def get_validator_code(self):
        return {self.code: self._patch_message({'min': self.min, 'max': self.max})}


class CallBackValidator(BaseBV):
    """
    Return the validity from a callback method

    http://bootstrapvalidator.com/validators/callback/
    """
    code = 'callback'

    def __init__(self, callback, message=None):
        """

        :param callback: the callback code or function name
        :return:
        """
        self.callback = callback
        self.message = message

    def get_validator_code(self):
        return {self.callback: self._patch_message({'callback': self.callback})}


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

    def __init__(self, country, message=None):
        self.country = country

    def get_validator_code(self):
        return {self.code: self._patch_message({'country': self.country})}


class EmailAddressValidator(BaseBV):
    code = 'emailAddress'

    def __init__(self, multiple=False, separator='/[,;]/', message=None):
        self.multiple = multiple
        self.separator = separator
        self.message = message

    def get_validator_code(self):
        return {self.code: self._patch_message({'multiple': str(self.multiple).lower(),
                                                'separator': self.separator})}


class UriValidator(BaseBV):
    code = 'uri'

    def __init__(self, allowLocal=False, protocol='http,https,ftp', message=None):
        self.allowLocal = allowLocal
        self.protocol = protocol
        self.message = message

    def get_validator_code(self):
        return {self.code: self._patch_message({'allowLocal': str(self.allowLocal).lower(),
                                                'protocol': self.protocol})}


class FileValidator(BaseBV):
    """
    Validate file

    :Warn The maxSize and type are only used if the browser supports HTML 5 File API.

    http://bootstrapvalidator.com/validators/file/
    """
    code = 'file'

    def __init__(self, extension, type=None, minSize=None, maxSize=None, message=None):
        self.extension = extension
        self.type = type
        self.minSize = minSize
        self.maxSize = maxSize
        self.message = message

    def get_validator_code(self):
        vc = {'extension': self.extension}
        if self.type:
            vc['type'] = self.type
        if self.minSize:
            vc['minSize'] = self.minSize
        if self.maxSize:
            vc['maxSize'] = self.maxSize

        return {self.code: self._patch_message(vc)}


class ImageFileValidator(FileValidator):
    def __init__(self, minSize=None, maxSize=None):
        super(ImageFileValidator, self).__init__('jpg,jpeg,png,bmp,gif,webp,ico,jnp',
                                                 'image/jpeg,image/png,images/gif,images/x-icon,images/x-ms-bmp,images/webp,images/x-jnp',
                                                 minSize, maxSize)


class VideoFileValidator(FileValidator):
    def __init__(self, minSize=None, maxSize=None):
        super(VideoFileValidator, self).__init__('mp4,3gp,3gpp,megp,mgp,mov,webm,flv,m4v,wmv,avi,',
                                                 'video/mp4,video/3gpp,video/mpeg,video/quicktime,video/x-flv,video/x-m4v,video/x-ms-wmv,video/x-msvideo,video/webm',
                                                 minSize, maxSize)


class AudioFileValidator(FileValidator):
    def __init__(self, minSize=None, maxSize=None):
        super(AudioFileValidator, self).__init__('mid,midi,kar,mp3,ogg,m4a,ra',
                                                 'audio/midi,audio/mpeg,audio/ogg,audio/x-m4a,audio/x-realaudio')

