from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Pages

# creamos el formulario a parte
#https://www.w3schools.com/tags/att_form_method.asp
FORMULARIO = """
	<form action="/" method="post">
	URL: <br>
	First name: <input type="text" name="name" placeholder="name"><br>
	Last name: <input type="text" name="page" placeholder="page"><br>
	<input type="submit" value="Submit">
	</form>
"""
def pages (request,num):

	try:
		page = Pages.objects.get(id = str(num))	
	except Pages.DoesNotExist:
		return HttpResponseNotFound('<h1>' + num + 'not found</h1>')
	return HttpResponse(page.name + str(page.page))
	
@csrf_exempt
def barra (request):

	if request.method == "POST":
		page  = Pages (name = request.POST['name'], page = request.POST['pages'])
		page.save()
	lista = Pages.objects.all()
	respuesta = "<ul>"
	for pagina in lista:
		respuesta += '<li><a href: "/pages/' + str(paginal.id) + '">' + pagina.name + "</a>" 
	respuesta = "</ul>"
	
	#  if request.user.is_authenticated():
    #   print("Logged in")
    #else:
     #   print("Not logged in")
	
	if request.user.is_authenticated():
	#https://stackoverflow.com/questions/12209438/logout-button-php/12209491
		logged = 'Logged in' + request.user.username + '<a href="logout.php">Logout</a>'
		respuesta = '<html><body><h1>' + logged + FORMULARIO + "</h1><p>" + respuesta + "</p></body></html>"
	else:
	#https://www.quora.com/How-does-one-link-login-php-and-register-php-in-index-phps-html-code
		logged = 'Not logged in <a href="login.php">Login</a>'
		respuesta = '<html><body><h1>' + logged + "</h1><p>" + respuesta + "</p></body></html>"
	return HttpResponse(respuesta)
