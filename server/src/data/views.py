from logging import log
from .log import get_logger
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Data
from django.db import DatabaseError
from django.db.models import Avg, Max, Min


logger = get_logger('data-views', 'data.log')


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def accept_data(request):
    if request.method == 'POST':
        client_ip = request.META.get('REMOTE_ADDR')
        print(client_ip)
        
        try:
            new_model = Data(
                ip_address=client_ip,
                cpu_load=request.POST['cpu_load']
            )
            new_model.save()

            logger.info(f'Written {new_model}')
        except DatabaseError as e:
            logger.error(str(e))

    objects = Data.objects.all().order_by('-id').all()

    context = {
        'data': objects[:100],
        'min_last': round(list(objects[:100].aggregate(Min('cpu_load')).values())[0], 2),
        'max_last': round(list(objects[:100].aggregate(Max('cpu_load')).values())[0], 2),
        'avg_last': round(list(objects[:100].aggregate(Avg('cpu_load')).values())[0], 2),
        'min_all': round(list(objects.aggregate(Min('cpu_load')).values())[0], 2),
        'max_all': round(list(objects.aggregate(Max('cpu_load')).values())[0], 2),
        'avg_all': round(list(objects.aggregate(Avg('cpu_load')).values())[0], 2),
    }
    return render(request, 'data.html', context)