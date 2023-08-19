import json
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Deals
from prepare_data import PrepareData

@csrf_exempt
def PipedrivePerson(request):
    try:
        if request.method == "GET":
            return render(request, "app/person.html")
        elif request.method == "POST":
            print(request.headers)
            print("\n\n --------->> DATA WEBHOOK - PERSON")
            body = json.loads(request.body)
            print(body)

            return JsonResponse({"code": 200, "msg": "success action webhook person - update"})
            
        return JsonResponse({"code": 401, "msg": "not-fould"})
    except Exception as e:
        print(f"ERROR WEBHOOK PERSON | ERROR: {e}")
        return JsonResponse({"code": 400, "msg": "error action webhook person"})
@csrf_exempt
def PipedriveDeals(request):
    try:
        if request.method == "GET":
            return render(request, "app/deals.html")
        elif request.method == "POST":
            print(request.headers)
            body = json.loads(request.body)
           
            # ---
            current = body["current"] # -------- subgrupo de dados
            current_id = int(current["id"])
            current_person_id = int(current["person_id"])
            current_owner_name = current["owner_name"]
            current_stage_id = int(current["stage_id"])
            current_active = current["active"]
            current_person_name = current["person_name"]
            current_status = current["status"]
            current_title = current["title"]
            current_org_name = current["org_name"]
            current_pipeline_id = int(current["pipeline_id"])
            current_value = float(current["value"])
            current_weighted_value  = float(current["weighted_value"])

            current_add_time = PrepareData.convert_string_to_datetime(current["add_time"])
            current_update_time = PrepareData.convert_string_to_datetime(current["update_time"])

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
            current_pipeline_id : {current_pipeline_id }
            current_org_name : {current_org_name }
            current_value : {current_value}
            current_weighted_value : {current_weighted_value}
            current_add_time : {current_add_time } | {type(current_add_time)}
            current_update_time : {current_update_time } | {type(current_update_time)}

            """)
            query_deal = Deals.objects.filter(current_id=current_id).first()
            print("\n ------------ query deals ------------ ")
            print(query_deal)
            if query_deal is not None:
                query_deal
                query_deal.current_id = current_id
                query_deal.current_person_id = current_person_id
                query_deal.current_owner_name = current_owner_name
                query_deal.current_stage_id = current_stage_id
                query_deal.current_active = current_active
                query_deal.current_person_name  = current_person_name
                query_deal.current_status  = current_status
                query_deal.current_title  = current_title
                query_deal.current_org_name  = current_org_name
                query_deal.current_pipeline_id  = current_pipeline_id
                query_deal.current_value  = current_value
                query_deal.current_weighted_value  = current_weighted_value
                query_deal.current_add_time  = current_add_time
                query_deal.current_update_time  = current_update_time
                query_deal.save()
                print(" --------->>> registro atualizado - deals ")
            else:
                new_deal = Deals.objects.create(
                    current_id=current_id,
                    current_person_id=current_person_id,
                    current_owner_name=current_owner_name,
                    current_stage_id=current_stage_id,
                    current_active=current_active,
                    current_person_name=current_person_name,
                    current_status=current_status,
                    current_title=current_title,
                    current_org_name=current_org_name,
                    current_pipeline_id=current_pipeline_id,
                    current_value=current_value,
                    current_weighted_value =current_weighted_value ,
                    current_add_time=current_add_time,
                    current_update_time=current_update_time
                )
                print("\n\n --------->>> criar registro - deals ")
                print(new_deal)

            



            return JsonResponse({"code": 200, "msg": "success action webhook deals - update"})
            
        return JsonResponse({"code": 401, "msg": "not-fould"})
    except Exception as e:
        print(f"ERROR WEBHOOK DEALS | ERROR: {e}")
        return JsonResponse({"code": 400, "msg": "error action webhook deals"})

