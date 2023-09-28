from .models import *
from rest_framework.viewsets  import ModelViewSet
from .serializers import PostSerializer, TranslationTestSerializer
from django.utils.translation import gettext_lazy as _

# Create your views here.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class TranslationTestViewSet(ModelViewSet):
    queryset = TranslationTest.objects.all()
    serializer_class = TranslationTestSerializer
    def get_serializer_class(self):
        serializer_class = super().get_serializer_class()

        if self.request and 'fr' in self.request.META.get('HTTP_ACCEPT_LANGUAGE', ''):
            serializer_class.Meta.fields =  ["prpo" if field == 'about'  else field.lower()  for field in serializer_class.Meta.fields]
            print( serializer_class.Meta.fields)
        return serializer_class
