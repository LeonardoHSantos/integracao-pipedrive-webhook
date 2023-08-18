import json
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt 

@csrf_exempt
def Deals(request):
    if request.method == "GET":
        return render(request, "app/deals.html")
    elif request.method == "POST":
        print(request.headers)
        body = json.loads(request.body)
        v = body["v"]
        meta = body["meta"]
        action = meta["action"]
        company_id = meta["company_id"]
        host = meta["host"]
        id_comp = meta["id"]
        object_hook = meta["object"]
        # ---
        current = body["current"]
        current_id = current["id"]
        current_person_id = current["person_id"]
        current_owner_name = current["owner_name"]
        current_stage_id = current["stage_id"]
        current_active = current["active"]
        current_person_name  = current["person_name"]
        current_status  = current["status"]
        current_title  = current["title"]
        current_update_time  = current["update_time"]
        current_pipeline_id  = current["pipeline_id"]
        current_weighted_value  = current["weighted_value"]
        current_org_name  = current["org_name"]
        current_value  = current["value"]
        current_add_time  = current["add_time"]

        print(f" --------------->> JSON/BODY: ")
        print(body)
        print(f"""
        \n ************ fields current ************
        current_id: {current_id}
        current_person_id: {current_person_id}
        current_owner_name: {current_owner_name}
        current_stage_id: {current_stage_id}
        current_active: {current_active}
        current_person_name : {current_person_name }
        current_status : {current_status }
        current_title : {current_title }
        current_update_time : {current_update_time }
        current_pipeline_id : {current_pipeline_id }
        current_weighted_value : {current_weighted_value }
        current_org_name : {current_org_name }
        current_value : {current_value }
        current_add_time : {current_add_time }
        """)



        return JsonResponse({"code": 200, "msg": "success action webhook deals - update"})
        
    
    return JsonResponse({"api": "error-deals"})

