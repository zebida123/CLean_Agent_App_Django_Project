from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .mpesa import initiate_stk_push

@csrf_exempt
def stk_push(request):
    if request.method != 'POST':
        return JsonResponse({'error':'POST required'}, status=400)
    phone = request.POST.get('phone')
    amount = request.POST.get('amount')
    if not phone or not amount:
        return JsonResponse({'error':'phone & amount required'}, status=400)
    try:
        res = initiate_stk_push(phone, amount)
    except Exception as e:
        return JsonResponse({'error':str(e)}, status=500)
    return JsonResponse(res)
