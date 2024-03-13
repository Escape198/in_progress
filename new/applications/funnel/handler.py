from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead


def handler(request) -> render:
    lead = Lead()

    for key in request:
        setattr(lead, key, request[key])

    lead.courseid_string = (
        ''.join(x for x in lead.courseid if not x.isdigit()))
    lead.save()

    return lead
