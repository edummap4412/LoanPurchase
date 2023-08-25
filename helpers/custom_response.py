

class CustomResponse:

    def __init__(self, data=None, status=200, errors=[], message='Success'):
        self._data = data
        self._status = status
        self._errors = errors
        self._pagination_data = None
        self._message = message

    def _prepare_response(self):
        _response = {
            'status': self._status,
            'message': self._message,
            'has_errors': False,
            'errors': self._errors,
        }

        if len(_response['errors']) > 0:
            _response['has_errors'] = True
            if _response['message'] == 'Success':
                _response['message'] = 'Failure'
            _response['status'] = self._status
        else:
            if _response['message'] == 'Success':
                _response['message'] = 'Success'

        if self._data is not None:
            if isinstance(self._data, dict):
                _response['result'] = self._data
            else:
                if self._pagination_data is None:
                    _response['results'] = self._data
                else:
                    _response = {**_response, **self._pagination_data}

        else:
            _response['result'] = None

        return _response

    def set_message(self, message):
        self._message = message

    def set_status(self, status):
        self._status = status

    def set_form_errors(self, data):
        self._errors = []
        for error in data:
            self._errors.append({'field': error, 'errors': data[error]})
        self._status = 400

    @property
    def response(self):
        return self._prepare_response()

    @property
    def status(self):
        return self._status
