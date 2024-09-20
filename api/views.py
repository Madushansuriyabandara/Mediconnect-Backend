from rest_framework.decorators import api_view
from rest_framework.response import Response
#from .serializers import NoteSerializer
from .models import Note

@api_view(['GET'])
def getRoutes(request):
    routes = [ ###
    ]
    return Response(routes)
