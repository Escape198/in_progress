import datetime
import traceback

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View

from applications.log.views import send_telegram_message
from applications.funnel.all_views.get_form import get_form


@csrf_exempt
def new_form(request):
    req = get_form(request)

    email, phone, name, product = req