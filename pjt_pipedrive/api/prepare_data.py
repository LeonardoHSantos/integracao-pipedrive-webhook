from datetime import datetime, timedelta


class PrepareData:
    def convert_string_to_datetime(dtime_string):
        try:
            list_string = list()
            for i in dtime_string:
                try:
                    if int(i)>=0:
                        list_string.append(i)
                except:
                    pass
            
            date_string = ''.join(list_string)
            date_time_obj = datetime.strptime(date_string, '%Y%m%d%H%M%S') - timedelta(hours=3)
            return date_time_obj
        except Exception as e:
            print(f" ### ERROR CONVERT STR TO DATETIME | ERROR: {e}")
            return None
    
    def dataDigits(data):
        aux_digits = list()
        for i in data:
            if i.isdigit():
                aux_digits.append(int(i))
        return aux_digits
    # ---
    def validateCPF(data):
        data_lead = None
        aux_validate = PrepareData.dataDigits(data=data)
        if len(aux_validate) == 11:
            data_lead = "".join(map(str, aux_validate))
        return data_lead
    # ---
    def validateCNPJ(data):
        data_lead = None
        aux_validate = PrepareData.dataDigits(data=data)
        if len(aux_validate) == 14:
            data_lead = "".join(map(str, aux_validate))
        return data_lead
    # ---
    def validatePHONE(data):
        data_lead = None
        aux_validate = PrepareData.dataDigits(data=data)
        if len(aux_validate) == 11:
            data_lead = "".join(map(str, aux_validate))
            data_lead = f"({data_lead[0:2]}) {data_lead[2:3]} {data_lead[3:7]}-{data_lead[7:]}"
        return data_lead
