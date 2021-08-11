from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET', 'POST'])
def accept_data(request):
    return render(request, 'data.html')