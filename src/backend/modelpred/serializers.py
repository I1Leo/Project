from rest_framework import serializers

class ParseSerializer(serializers.Serializer):
   
   excel_file = serializers.FileField(required=True)