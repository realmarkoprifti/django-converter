from django.shortcuts import render
from decouple import config
from .models import Coin
import requests

API_KEY = config("API_KEY")

# Create your views here.

def index(request):
    if request.method == "GET":
        
        return render(request, "currency/index.html", {
            "options": Coin.objects.all()
        })
        
    elif request.method == "POST":
        url = "https://free.currconv.com/api/v7/convert?q=USD_PHP,PHP_USD&compact=ultra&apiKey=" + API_KEY
        try:
            amount = float(request.POST["amount"])
            
        except:
            return render(request, "currency/index.html", {
            "options": Coin.objects.all()
        })
              
        frm = request.POST["from"]
        to = str(request.POST["to"])
        frmlist = frm.split(', ')
        tolist = to.split(', ')
        url = str(url).replace("USD_PHP,PHP_USD", f"{frmlist[0]}_{tolist[0]}")
        response = requests.get(url)
        json = response.json()
        number = float(json[f"{frmlist[0]}_{tolist[0]}"]) * amount
        two_point_num = '{:.2f}'.format(number) 
        final = f"{float(two_point_num):,}"
        
        return render(request, "currency/result.html", {
            "result": f"{str(final)} {tolist[0]}"
        })