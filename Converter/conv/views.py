from django.shortcuts import render
from django.http import JsonResponse
from .conv import get_values

# Create your views here.

def convert(request, arg1, arg2):
    val1, val2, date = get_values(arg1,arg2)
    answer = {"result" :
              {
                  "date": str(date),
                  "rate": round(val1/val2,4)
                  }
        }
    return JsonResponse(answer)
