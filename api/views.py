
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TodoSerializer
from .models import Todo


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getTodos(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createTodo(request):
    data = request.data
    todo = Todo.objects.create(body=data['body'])
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
def updateTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTodo(request, pk):
    Todo.objects.get(id=pk).delete()
    return Response("Note was deleted!")
