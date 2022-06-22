from django.http import HttpResponse

#Aqui va la función que llama a la vista
def Vista(request): #primera vista
    return HttpResponse("Hola Mundo, estoy probando Django") 