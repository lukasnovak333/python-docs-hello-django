""" 
	bossServices.py - Implements basic services 
	for the boss application. 
"""


# Python Imports
import json 
import sys
import time
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
		body_unicode = request.body.decode('utf-8')
		content = json.loads(body_unicode)

		resultsObj = {}

		for key in ['cond', 'id', 'R1','R2', 'R3', 'R4', 'R5', 'R6', 'total', 'surveyResults', 'debriefFunnel']:
			if key not in content:
				return JsonResponse({'error': 'true', 'message': 'no' + key})
			else:
				resultsObj[key] = content[key]


		f= open("/home/site/textFiles/db.txt","a+")
		f.write('---------------\n')
		f.write(time.ctime(time.time()) + '\n')
		f.write(json.dumps(resultsObj, indent=4))
		f.write('\n----------------')
		f.close()
		return JsonResponse({'success': "true"})

	except Exception as e:
		return JsonResponse({'error': 'true', 'message': e})

	
