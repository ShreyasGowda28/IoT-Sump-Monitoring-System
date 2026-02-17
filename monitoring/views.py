from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SumpReading
from .serializers import SumpReadingSerializer


@api_view(["POST"])
def receive_sump_data(request):
    serializer = SumpReadingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Data saved successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render
from .models import SumpReading

def dashboard(request):
    readings = SumpReading.objects.order_by('-timestamp')[:10]
    return render(request, 'dashboard.html', {'readings': readings})
