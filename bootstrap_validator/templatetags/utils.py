def convert_datetime_python_to_javascript(input_format):
    input_format = input_format.replace('%Y', 'YYYY')
    input_format = input_format.replace('%m', 'MM')
    input_format = input_format.replace('%d', 'DD')
    input_format = input_format.replace('%H', 'h')
    input_format = input_format.replace('%M', 'm')
    input_format = input_format.replace('%S', 's')
    return input_format