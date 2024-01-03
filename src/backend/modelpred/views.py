from django.shortcuts import render
from django.core.files.storage import default_storage
from django.conf import settings

# Create your views here.
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from modelpred.serializers import ParseSerializer

from modelpred.source_code.model import Model

class PredictView(GenericViewSet):

   serializer_class = ParseSerializer

   @action(methods=['POST'], detail=False)
   def predict(self, request, *args, **kwargs):

      serializer = self.serializer_class(data=request.data)
      serializer.is_valid(raise_exception=True)

      excel_file = default_storage.save(serializer.validated_data['excel_file'].name, serializer.validated_data['excel_file'])
      excel_filePath = '/'.join([settings.MEDIA_ROOT, excel_file]);

      model = Model(excel_filePath)
      response = model.run()
      
      if 'Postman' in request.META.get('HTTP_USER_AGENT', ''):
            return Response({'result': response})
      else:
            return render(request, 'pages/main.html', {'result': response})
