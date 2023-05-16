from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def flight(request):
    if request.method == 'GET':
        flight_info = {
            'id': 1,
            'flight_number': 'ABC123',
            'departure_city': 'New York',
            'arrival_city': 'Los Angeles',
            'departure_date': '2023-05-20',
            'arrival_date': '2023-05-20',
            'passengers': ['John Doe', 'Jane Smith'],
        }
        return JsonResponse(flight_info)
    else:
        return HttpResponseBadRequest('Invalid request method')


@require_http_methods(["GET", "POST"])
def airline(request):
    if request.method == 'GET':
        airline_info = {
            'id': 1,
            'name': 'Sample Airlines',
            'established_date': '2010-01-01',
        }
        return JsonResponse(airline_info)
    else:
        return HttpResponseBadRequest('Invalid request method')


@require_http_methods(["GET", "POST"])
def airport(request):
    if request.method == 'GET':
        airport_info = {
            'id': 1,
            'name': 'Sample Airport',
            'city': 'New York',
            'country': 'United States',
            'code': 'JFK',
        }
        return JsonResponse(airport_info)
    else:
        return HttpResponseBadRequest('Invalid request method')