from django.http import JsonResponse
from guestcomment.models import Guest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict
from guestcomment.serializers import GuestSerializer,GuestSerializerPost
from colors import Bcolors as C


@api_view(["GET"])
def api_guest_model(request, *args, **kwargs):
    model_data = Guest.objects.all()
    data_array=[]
    data = {"data":data_array}
    if model_data:
        for each in model_data:
            data_array.append(model_to_dict(each, fields=["id", "first_name", "last_name", "comment"]))
    return JsonResponse(data)

@api_view(["GET"])
def api_guest_serializer(request, *args, **kwargs):
    instance = Guest.objects.all()
    data_array=[]
    data = {"data":data_array}
    if instance:
        for each in instance:
            data_array.append(GuestSerializer(each).data)
            print(C.YLW, data, C.ENDC)
    return Response(data)

@api_view(["POST"])
def api_guest_serializer_post(request, *args, **kwargs):
    print(C.GRNBLDRK, request.data, C.ENDC)
    serializer = GuestSerializerPost(data=request.data)
    data = {}
    if serializer.is_valid():
        instance = serializer.save()
        data = serializer.data
    return Response(data)