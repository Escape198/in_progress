

def get_form(request) -> list:
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    name = request.POST.get('name', '')
    product = request.POST.get('product', '')

    return [email, phone, name, product]