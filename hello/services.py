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
@require_http_methods(["POST"])
def single_service(request):
	""" This is a service, defined in urls.py, and 
	    called via ajax methods (e.g. fetch)
	    You can do things with the database, and return 
	    the results. 
	    Basically, urls.py tells the server what to do 
	    with a given request. There, you can tell the 
	    server: "whenever you receive a url that ends in /contact/aService",
	     come here, and call this function.
	    The function receives the request as an argument! 
	    Isn't Django nice? It can also be passed arguments,
	    like the net_id that was parsed from the URL. 
	    The function then returns something, and that's 
	    what you'll receive in your javascript environment
	    when the fetch call (or whatever ajax call you use)
	    returns. 
	"""

	try:
		return JsonResponse({'body': request})
		
		content = request.body
		cond_and_id = content['conditionAndId']
		final_result = content['finalResult']


		f= open("/home/site/textFiles/tmptest.txt","a")
		f.write('----------------')
		f.write('condition and Id - {}'.format(cond_and_id))
		f.write('finalResult - {}'.format(final_result))
		f.write('----------------')
		f.close()
		return JsonResponse({'success': "true"})

	except Exception as e:
		return JsonResponse({'error': 'true', 'message': e})

	
