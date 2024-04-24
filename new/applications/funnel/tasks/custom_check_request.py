import datetime

from log.models import Spammers
from log.views import send_error


MALICIOUS_WORDS = ['<', '>', 'script', '&gt', '&le', '&ge']
UNWANTED_REFERERS = ['url1', 'url2']


def check_request(request) -> bool:
    """
    Общая логика обработки запроса.

    bool - Является ли фейком
    """
    try:
        ip = request.META.get('HTTP_X_REAL_IP', '')
        request_post = request.POST
        name = request_post.get('name', '')
        phone = request_post.get('phone', '')
        email = request_post.get('email', '')

        if (
            has_malicious_code(request_post, name)
            or has_unwanted_referer(request.META.get('HTTP_REFERER', ''))
            or is_in_spammers_db(email, phone, ip)
        ):
            create_spammer_record(request_post, name, email, ip, phone)
            return True

    except Exception:
        send_error(request.POST, exc='unknown')
        return True

    return False


def has_malicious_code(request_post, name) -> bool:
    """
    Проверяет наличие вредоносного кода в запросе.

    bool - Является ли фейком
    """
    request_str = str(request_post).replace(']}>', '').replace('<QueryDict', '')
    return len(name) > 70 or any(word in request_str for word in MALICIOUS_WORDS)


def has_unwanted_referer(referer_url) -> bool:
    """
    Проверяет нежелательный Referer в запросе.

    bool - Является ли фейком
    """
    return not referer_url or not any(unwanted in referer_url for unwanted in UNWANTED_REFERERS)


def is_in_spammers_db(email, phone, ip) -> bool:
    """
    Проверяет, находится ли адрес электронной почты, номер телефона или IP-адрес в базе данных.

    email: Адрес электронной почты
    phone: Номер телефона
    ip: IP-адрес

    bool - Является ли фейком
    """
    return (
        Spammers.objects.filter(email=email).exists()
        or Spammers.objects.filter(phone=phone).exists()
        or Spammers.objects.filter(ip=ip).exists()
    )


def create_spammer_record(request_post, name, email, ip, phone) -> None:
    """
    Добавляет запись о подозрительном запросе в базу данных.

    request_post: POST-параметры запроса
    name: Имя пользователя
    email: Адрес электронной почты
    ip: IP-адрес
    phone: Номер телефона
    """
    if name and email and ip and phone:
        Spammers.objects.create(
            time=datetime.datetime.now(),
            request=request_post,
            name=name,
            email=email,
            ip=ip,
            phone=phone
        )
