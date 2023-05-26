from django.shortcuts import render
# Create your views here.
import csv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Transaction

@csrf_exempt
def upload_csv(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        if file.name.endswith('.csv'):
            data = csv.DictReader(file)
            for row in data:
               transaction = Transaction(
                   transaction_id = row['Transaction ID'],
                   transaction_date = row['Transaction Date'],
                   transaction_amount = row['Transaction Amount'],
                   transaction_category = row['Merchant Name']
               )
               transaction.save()
               return JsonResponse({'message': 'CSV file uploaded successfully.'})
            else:
                return JsonResponse({'error': 'Invalid file format. Please upload a CSV file.'})
        else:
            return JsonResponse({'error': 'POST request with file parameter is required.'})