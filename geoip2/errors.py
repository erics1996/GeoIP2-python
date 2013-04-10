"""
Errors
======

"""


class GeoIP2Error(RuntimeError):
    """There was a generic error in GeoIP2.

    This class represents a generic error. It extends :py:exc:`RuntimeError`
    and does not add any additional attributes.

    """


class GeoIP2HTTPError(GeoIP2Error):
    """There was an error when making your HTTP request.

    This class represents an HTTP transport error. It extends 
    :py:exc:`GeoIP2Error` and adds attributes of its own.

    :ivar http_status: The HTTP status code returned
    :ivar uri: The URI queried
    """
    def __init__(self, message, http_status=None, uri=None):
        super(GeoIP2HTTPError, self).__init__(message)
        self.http_status = http_status
        self.uri = uri


class GeoIP2WebServiceError(GeoIP2HTTPError):
    """The GeoIP2 web service returned an error.

    This class represents an error returned by MaxMind's GeoIP2 Precision
    web service. It extends :py:exc:`GeoIP2HTTPError`.

    :ivar code: The code returned by the MaxMind web service
    :ivar http_status: The HTTP status code returned
    :ivar uri: The URI queried

    """
    def __init__(self, message, code=None, http_status=None, uri=None):
        super(GeoIP2WebServiceError, self).__init__(message, http_status, uri)
        self.code = code
