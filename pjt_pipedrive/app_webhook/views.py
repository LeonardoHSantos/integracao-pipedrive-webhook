import json
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt 

@csrf_exempt
def Deals(request):
    if request.method == "GET":
        return render(request, "app/deals.html")
    elif request.method == "POST":
        body = json.loads(request.body)
        header_post = request.POST
        print(f" --------------->> JSON/BODY: ")
        print(body)
        print(f" --------------->> HEADER/BODY: ")
        print(header_post)
        return JsonResponse({"api": "deals"})
    
    return JsonResponse({"api": "error-deals"})

