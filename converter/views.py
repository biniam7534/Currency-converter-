import requests
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    # Fetch list of currencies for the dropdown
    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        data = response.json()
        currencies = list(data['rates'].keys())
    except Exception as e:
        currencies = ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD']
    
    return render(request, 'index.html', {'currencies': currencies})

def convert(request):
    if request.method == 'GET':
        from_curr = request.GET.get('from')
        to_curr = request.GET.get('to')
        amount = request.GET.get('amount')
        
        if not all([from_curr, to_curr, amount]):
            return JsonResponse({'error': 'Missing parameters'}, status=400)
            
        try:
            amount = float(amount)
            url = f'https://api.exchangerate-api.com/v4/latest/{from_curr}'
            response = requests.get(url)
            data = response.json()
            rate = data['rates'][to_curr]
            result = amount * rate
            
            return JsonResponse({
                'result': round(result, 2),
                'rate': rate,
                'from': from_curr,
                'to': to_curr
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
