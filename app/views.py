from django.shortcuts import render
import requests
# Create your views here.

def list(request):
	url = "https://api.github.com/events"
	response = requests.get(url).json()

	context = {
	"response": response
	}
	return render(request,"list.html", context)