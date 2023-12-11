from django.http import JsonResponse
from rest_framework import generics
from guestcomment.serializers import GuestSerializer,GuestSerializerPost
from guestcomment.models import Guest


class GuestListAPIView(generics.ListAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


class GuestListCreateAPIView(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializerPost


class GuestDetailAPIView(generics.RetrieveAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class GuestCreateAPIView(generics.CreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializerPost


class GuestUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializerPost