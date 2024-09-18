from rest_framework.decorators import api_view
from rest_framework.response import Response
#from .serializers import NoteSerializer
from .models import Note

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method':'GET',
            'body':None,
            'description':'Returns an array of notes'

        },

        {
            'Endpoint': '/notes/id',
            'method':'GET',
            'body':None,
            'description':'Returns a single note object'

        },

        {
            'Endpoint': '/notes/create/',
            'method':'POST',
            'body':{'body':""},
            'description':'Creates new note with data sent in post request'

        },

        {
            'Endpoint': '/notes/id/update/',
            'method':'PUT',
            'body':{'body':""},
            'description':'Creates an existing note with data sent in request'

        },
        {
            'Endpoint': '/notes/id/delete/',
            'method':'DELETE',
            'body': None,
            'description':'Delete an existing note'

        },
    ]
    return Response(routes)