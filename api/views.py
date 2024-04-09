# myapp/views.py
import random
import string

from django.http import Http404, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TestData
from .serializers import TestDataSerializer


class TestJsonAPIView(APIView):
    def generate_random_url(self):
        characters = string.ascii_letters + string.digits + '4a718cf939709c927103b326f2e23b4d'
        return ''.join(random.choices(characters, k=10))  # Adjust the length of the URL as needed

    def post(self, request):
        url = self.generate_random_url()
        data = {'url': url, 'json_data': request.data}  # Ensure that request.data is a dictionary
        serializer = TestDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"url": url}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, url=None):
        if url:
            try:
                test_data = TestData.objects.get(url=url)
                json_data = test_data.json_data
                return JsonResponse(json_data, safe=False)
            except TestData.DoesNotExist:
                raise Http404("Data not found.")
        else:
            return Response({"detail": "Specify a URL."}, status=status.HTTP_400_BAD_REQUEST)
