def get_field(request):
    try:
        field = request['sort']
    except (KeyError, ValueError, TypeError):
        field = ''
    return (request.direction == 'desc' and '-' or '') + field

def get_direction(request):
    try:
        return request['dir']
    except (KeyError, ValueError, TypeError):
        return 'desc'

class SortingMiddleware(object):
    """
    Inserts a variable representing the field (with direction of sorting)
    onto the request object if it exists in either **GET** or **POST**
    portions of the request.
    """
    def process_request(self, request):
        request.__class__.field = property(get_field)
        request.__class__.direction = property(get_direction)
