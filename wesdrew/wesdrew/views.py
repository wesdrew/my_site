from django.shortcuts import render
from utilities.file_to_dict import file_to_dict


def index(request):
    """
    Just a simple page using a template for now 

    """
    d = file_to_dict("|", "static/text/front_page")
    return render(request, 'about.html', d)

    
