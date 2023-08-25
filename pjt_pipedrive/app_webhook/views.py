import json
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Deals, Person
from api.prepare_data import PrepareData
from api.api_pipedrive import API_Pipedrive
from config_app import API_TOKEN, COMPANY_DOMAIN


def home(request):
    if request.method == "GET":
        query_person = Person.objects.all()
        context = {
            "person": query_person
        }
        # print(context)
        return render(request, "app/home.html", context=context)
# ---
def about(request):
    if request.method == "GET":
        return render(request, "app/about.html")
# ---
def infoServices(request, service_name):
    if request.method == "GET":
        context = {
            "service_name": service_name
        }
        return render(request, "app/home.html", context=context)


def infoPerson(request, id_person):
    API = API_Pipedrive(api_token=API_TOKEN, company_domain=COMPANY_DOMAIN)
    if request.method == "GET":
        person = API.get_person(person_id=int(id_person))
        if person["code"] == 200:
            context = {
                "data": person["data"],
                "data_resume": person["data_resume"],
            }
            # print(context)
            return render(request, "app/infoPerson.html", context=context)
        else:
            context = {
                "code": 400,
                "data": "error",
                "not_found_data": True,
            }
            return render(request, "app/infoPerson.html", context=context)

    elif request.method == "POST":
        r = dict(request.POST)
        # print(r)
        phone = r.get("phone")
        select_type_phone = r.get("select_type_phone")
        email = r.get("email")
        select_type_email = r.get("select_type_email")

        obj_update = {
            "name": r.get("name")[0],
            "phone": [],
            "email": [],
        }
        
        for i in range(len(phone)):
            obj_update.get("phone").append(
                {
                    "label": select_type_phone[i],
                    "value": phone[i]
                })
        for i in range(len(email)):
            obj_update.get("email").append(
                {
                    "label": select_type_email[i],
                    "value": email[i]
                })

        # print("\n\n\n\n *************** DATA POST")
        # print(obj_update)
        API.update_person(person_id=id_person, data=obj_update)
        person = API.get_person(person_id=int(id_person))

        if person["code"] == 200:
            context = {
                "data": person["data"],
                "data_resume": person["data_resume"],
            }
            return render(request, "app/infoPerson.html", context=context)
        else:
            context = {
                "code": 400,
                "data": "error",
                "not_found_data": True,
            }
            return render(request, "app/infoPerson.html", context=context)
    
@csrf_exempt
def PipedrivePerson(request):
    try:
        if request.method == "GET":
            query_person = Person.objects.all()
            context = {
                "person": query_person
            }
            # print(context)
            return render(request, "app/person.html", context=context)
        elif request.method == "POST":
            # print(request.headers)
            # print("\n\n --------->> DATA WEBHOOK - PERSON")
            body = json.loads(request.body)
            # print(body)
            current = body["current"]
            # ---
            current_id = int(current["id"])
            current_name = current["name"]
            current_owner_name = current["owner_name"]
            current_open_deals_count = int(current["open_deals_count"])
            current_email = current["email"][0]["value"]
            current_phone = current["phone"][0]["value"]
            current_add_time = PrepareData.convert_string_to_datetime(current["add_time"])
            current_update_time = PrepareData.convert_string_to_datetime(current["update_time"])

            print(f"""
            --> current_id: {current_id} | {type(current_id)}
            --> current_name: {current_name} | {type(current_name)}
            --> current_owner_name: {current_owner_name} | {type(current_owner_name)}
            --> current_open_deals_count: {current_open_deals_count} | {type(current_open_deals_count)}
            --> current_email: {current_email} | {type(current_email)}
            --> current_phone: {current_phone} | {type(current_phone)}
            --> current_add_time: {current_add_time} | {type(current_add_time)}
            --> current_update_time: {current_update_time} | {type(current_update_time)}
            """)
            query_person = Person.objects.filter(current_person_id=current_id).first()
            print("\n ------------ query person ------------ ")
            print(query_person)
            if query_person is not None:
                query_person.current_person_id = current_id
                query_person.current_person_name = current_name
                query_person.current_person_owner_name = current_owner_name
                query_person.current_person_open_deals_count = current_open_deals_count
                query_person.current_person_email = current_email
                query_person.current_person_phone = current_phone
                query_person.current_person_add_time = current_add_time
                query_person.current_person_update_time = current_update_time
                query_person.save()
                print(" --------->>> registro atualizado - person ")
            else:
                new_person = Person.objects.create(
                    current_person_id=current_id,
                    current_person_name=current_name,
                    current_person_owner_name=current_owner_name,
                    current_person_open_deals_count=current_open_deals_count,
                    current_person_email=current_email,
                    current_person_phone=current_phone,
                    current_person_add_time=current_add_time,
                    current_person_update_time=current_update_time
                )
                # new_person.save()
                print("\n\n --------->>> registro criado - person ")
                print(new_person)
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
            query_deal = Deals.objects.filter(current_deal_id=current_id).first()
            print("\n ------------ query deals ------------ ")
            print(query_deal)
            person = Person.objects.filter(current_person_id=current_person_id).first()
            print("\n ------------ query person ------------ ")
            print(person)

            if person is None:
                person = Person.objects.create(
                    current_person_id=current_person_id,
                    current_person_name=current_person_name,
                    current_person_add_time=current_add_time,
                    current_person_update_time=current_update_time,
                    )
                person.save()
                person = Person.objects.filter(current_person_id=current_person_id).first()
            print(f" PERSON: {person}")
            if query_deal is not None:            
                query_deal.current_deal_id = current_id
                query_deal.current_deal_person_id = current_person_id
                query_deal.current_deal_owner_name = current_owner_name
                query_deal.current_deal_stage_id = current_stage_id
                query_deal.current_deal_active = current_active
                query_deal.current_deal_person_name  = current_person_name
                query_deal.current_deal_status  = current_status
                query_deal.current_deal_title  = current_title
                query_deal.current_deal_org_name  = current_org_name
                query_deal.current_deal_pipeline_id  = current_pipeline_id
                query_deal.current_deal_value  = current_value
                query_deal.current_deal_weighted_value  = current_weighted_value
                query_deal.current_deal_add_time  = current_add_time
                query_deal.current_deal_update_time  = current_update_time
                query_deal.save()
                print(" --------->>> registro atualizado - deals ")
            else:
                new_deal = Deals.objects.create(
                    person=person,
                    current_deal_id=current_id,
                    current_deal_person_id=current_person_id,
                    current_deal_owner_name=current_owner_name,
                    current_deal_stage_id=current_stage_id,
                    current_deal_active=current_active,
                    current_deal_person_name=current_person_name,
                    current_deal_status=current_status,
                    current_deal_title=current_title,
                    current_deal_org_name=current_org_name,
                    current_deal_pipeline_id=current_pipeline_id,
                    current_deal_value=current_value,
                    current_deal_weighted_value =current_weighted_value ,
                    current_deal_add_time=current_add_time,
                    current_deal_update_time=current_update_time
                )
                print("\n\n --------->>> registro criado - deals ")
                # new_deal.save()
                print(new_deal)

            



            return JsonResponse({"code": 200, "msg": "success action webhook deals - update"})
            
        return JsonResponse({"code": 401, "msg": "not-fould"})
    except Exception as e:
        print(f"ERROR WEBHOOK DEALS | ERROR: {e}")
        return JsonResponse({"code": 400, "msg": "error action webhook deals"})

