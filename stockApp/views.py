from django.shortcuts import render
from django.http import  Http404
from .models import Stocks
import requests
from bs4 import BeautifulSoup
import pandas as pd
from .active_stock_scrapper import run
from .management.commands.load_stocks_data import CopyToDatabase
from .neural_stuff import predict_stock

def home(request):
    run()
    CopyToDatabase()
    return render(request,'home.html')

def activeS(request):
    stocks = Stocks.objects.all()
    return render(request,'active_stocks.html',{
        'stocks': stocks,
    })

def stock_detail(request,stock_id):
    try:
        # predict_stock('AAP')
        stock = Stocks.objects.get(id=stock_id)
    except Stocks.DoesNotExist:
        raise Http404('Stock not found')
    return render(request, 'stock_detail.html',{
        'stock' : stock,
    })
