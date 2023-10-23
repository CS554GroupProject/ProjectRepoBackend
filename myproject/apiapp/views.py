from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from .third_party_interfaces import get_completion


class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class GetResponse:
    """class to get responses"""
    def recipe_suggestion(self, prompt:str):
        """This function takes in a prompt and returns a response"""
        response = None
        response = get_completion(prompt)
        return response
    
class Home:
    """Class to interact with the home page"""
    def home(request):
