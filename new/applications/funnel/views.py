from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from rest_framework.request import Request

from paid_funnel.custom_check_request import check_request

from log.views import send_error
from paid_funnel.views.handler import handler


@require_POST
@csrf_exempt
def paid_funnel(request: Request) -> render:
    try:
        if check_request(request, name=request.POST.get('name', '')):
            return JsonResponse({"code": 400})

        response = handler(request)
        return response

    except Exception:
        send_error(request.POST, exc='unknown')
        return render(request, '500.html')
