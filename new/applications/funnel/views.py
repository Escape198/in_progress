from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.request import Request

from log.views import send_error
from funnel.tasks.handler import handler
from funnel.decorators import fraud_filter_decorator


class PaidFunnel(View):
    """Воронка платных продуктов"""
    @staticmethod
    @fraud_filter_decorator
    def post(request):
        try:
            return handler(request)
        except Exception:
            send_error(request.POST, exc='unknown')

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(PaidFunnel, self).dispatch(*args, **kwargs)


def courses_with_open_date(request: Request) -> render:
    """Вывод для продуктов, недоступных к оплате"""
    return render(request, 'pay/new_open_date.html')
