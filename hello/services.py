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

# Our content
# from ..models import *


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
	return JsonResponse({'success': "true"})
