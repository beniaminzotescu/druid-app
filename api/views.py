# myapp/views.py
import random
import string
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TestData
from .serializers import TestDataSerializer

class TestJsonAPIView(APIView):
    def generate_random_url(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=10))  # Adjust the length of the URL as needed

    def post(self, request):
        url = self.generate_random_url()
        serializer = TestDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(url=url)  # Save the generated URL with the data
            return Response({"url": url}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, url=None):
        if url:
            test_data = TestData.objects.filter(url=url).first()
            if test_data:
                serializer = TestDataSerializer(test_data)
                return Response(serializer.data)
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Handle request without a specific URL
            return Response({"detail": "Specify a URL."}, status=status.HTTP_400_BAD_REQUEST)
