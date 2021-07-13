from django.http import HttpResponse


def home(request):
   
    return HttpResponse("""Use the django admin to add people with their resepective roles and 
                           then use the django shell to interact with the manager, for example <b> Person.people.editors() </b> """)
