import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def contact_submit(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)

    try:
        # Use request.POST to read form fields
        subject = request.POST.get('subject')
        recipients = request.POST.get('recipients')
        body = request.POST.get('body')
        subtype = request.POST.get('subtype')
        domain = request.POST.get('domain')

        payload = {
            "subject": subject,
            "recipients": recipients,
            "body": body,
            "subtype": subtype,
            "domain": domain
        }

        headers = {
            "api-key": "4a88171b7006e4d33fbc8cc94fd96aae6abed"
        }

        response = requests.post("https://apim.creditbureau.com.kh/uat-notify-api/api/v2/email/send", headers=headers, data=payload)

        if response.status_code == 200:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': response.text}, status=response.status_code)

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)
