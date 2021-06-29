from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def hello(request):
    """ Serve the page for viewing a user profile. 
    """
    context = {
        'props': {
        	'info': [  
                '''
                    ./application_name/services.py is where we define any asynchronous
                    services we want to provide
                ''',
                '''
                    Have fun!
                '''
            ]
        }
    }

    return render(request, "base.html", context=context)
