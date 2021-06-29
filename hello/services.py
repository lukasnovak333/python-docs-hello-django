""" 
	bossServices.py - Implements basic services 
	for the boss application. 
"""


# Python Imports
import json 
import sys
sys.path.append("..")

# Basic Django Tools
from django.http import QueryDict, JsonResponse

# Service Decorators
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

# Our content
# from .models import *

@csrf_exempt
# @require_http_methods(["POST"])
def single_service(request):
	try:
		if 'body' not in request:
			return JsonResponse({'error': 'true', 'message': 'nobodyfound'})

		content = request['body']

		if 'conditionAndId' not in content:
			return JsonResponse({'error': 'true', 'message': 'nocondandid'})

		cond_and_id = content['conditionAndId']

		if 'finalResult' not in content:
			return JsonResponse({'error': 'true', 'message': 'nocondandid'})

		final_result = content['finalResult']


		f= open("/home/site/textFiles/tmptest.txt","w+")
		f.write('----------------')
		f.write('condition and Id - {}'.format(cond_and_id))
		f.write('finalResult - {}'.format(final_result))
		f.write('----------------')
		f.close()
		return JsonResponse({'success': "true"})

	except Exception as e:
		return JsonResponse({'error': 'true', 'message': e})

	
