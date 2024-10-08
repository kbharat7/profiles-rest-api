from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets

class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer
    """Test API View"""
    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions(get,post,patch,delete)',
            'Is similar to a traditional django view',
            'Gives you most control over app logic',
            'Is mapped manually to URLs'
        ]

        return Response({"Message": "Hello", "an_apiview":an_apiview})

    def post(self,request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handle updating Object"""
        return Response({"method": "PUT"})

    def patch(self,request,pk=None):
        """Handle partial update of an object"""
        return Response({"method": "PATCH"})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({"method": "DELETE"})

class HelloViewSet(viewsets.ViewSet):
    serializer_class =serializers.HelloSerializer
    """Test API ViewSet"""
    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses Actions as functions(list,create,retrieve,update,partial_update)',
            'Automatically maps to URLs using routers',
            'Provides more functionality with less code',
        ]
        return Response({"message": "Hello","a_viewset": a_viewset})
    def create(self,request):
        """Create a new Hello Message"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f"Hello {name}!"
            return Response({"message": message})

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """Handle getting an object by its ID"""
        return Response({"HTTP_METHOD": "GET"})

    def update(self,request,pk=None):
        """Handle updating an object by its ID"""
        return Response({"HTTP_METHOD": "PUT"})

    def partial_update(self,request,pk=None):
        """Handle updating part of an object by its ID"""
        return Response({"HTTP_METHOD": "PATCH"})


    def destroy(self,request,pk=None):
        """Handle delete an object by its ID"""
        return Response({"HTTP_METHOD": "DELETE"})





