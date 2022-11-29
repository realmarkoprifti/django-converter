from django.shortcuts import render
from decouple import config

API_KEY = config("API_KEY")

# Create your views here.

def index(request):
    return render(request, "currency/index.html", {
        "input":'''<form action="" class="col-4">
                    <div class="row">

                        <label for="Amount" class="col-12"><b>Amount</b></label><br>

                        <div class="col-2"></div>
                        <input  class="col-8" type="text" id="Amount"><br><br>
                        <div class="col-2"></div>

                        <label for="from" class="col-12"><b>From</b></label><br>

                        <div class="col-2"></div> 
                        <select class="col-8">
                            <option value="EU">EU</option>
                            <option value="EU">EU</option>
                            <option value="EU">EU</option>
                            <option value="EU">EU</option>
                        </select><br><br>
                        <div class="col-2"></div>

                        <label for="to" class="col-12"><b>To</b></label><br>

                        <div class="col-2"></div>

                        <select class="col-8">
                            <option value="EU">EU</option>
                            <option value="EU">EU</option>
                            <option value="EU">EU</option>
                            <option value="EU">EU</option>
                        </select><br><br>

                        <div class="col-2"></div>

                        <div class="col-3"></div>
                        <input class="col-6" id="convert" type="button" value="Convert">
                        <div class="col-3"></div>

                    </div>
                </form>'''
    })