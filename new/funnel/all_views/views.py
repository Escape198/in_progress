import datetime
import traceback

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from log.views import send_telegram_message


def get_form(request) -> list:
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    name = request.POST.get('name', '')
    product = request.POST.get('product', '')

    return [email, phone, name, product]


@csrf_exempt
def new_form(request) -> render:
    req = get_form(request)

    email, phone, name, product = req
