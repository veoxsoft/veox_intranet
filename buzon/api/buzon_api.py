import buzon.helpers.json_serializer as serializer

from django.views.generic import View
from django.http import HttpResponse, JsonResponse

from buzon.models import Buzon
from buzon.dtos.response_dto import ResponseDto


class BuzonApi(View):
    def get(self, request):
        try:
            buzones = Buzon.objects.all()
            print(buzones)
            return JsonResponse(serializer.to_json(ResponseDto(data=buzones)), safe=False)
        except Exception as e:
            return JsonResponse(serializer.to_json(ResponseDto(status=False, message=str(e))), safe=False)

    def post(self, request):
        try:
            if buzon.is_valid():
                buzon.save()
            return JsonResponse(serializer.to_json(
                ResponseDto()), safe=False)
        except Exception as e:
            return JsonResponse(serializer.to_json(ResponseDto(status=False, message=str(e))), safe=False)
