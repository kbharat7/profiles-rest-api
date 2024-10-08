from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
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




