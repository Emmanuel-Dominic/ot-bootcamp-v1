from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ActivitySerializer
from .models import Activity


# Create your views here.
class ActivityAPIView(APIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    # http_method_names = ['GET', 'POST', 'PATCH',]

    def get(self, request):
        activities = Activity.objects.all()
        serializer = self.serializer_class(activities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request):
        data = request.DATA
        qs = Activity.objects.filter(id=1)
        serializer = self.serializer_class(qs, data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
