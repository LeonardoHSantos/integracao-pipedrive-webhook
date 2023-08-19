from datetime import datetime


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
            date_time_obj = datetime.strptime(date_string, '%Y%m%d%H%M%S')
            return date_time_obj
        except Exception as e:
            print(f" ### ERROR CONVERT STR TO DATETIME | ERROR: {e}")
            return None