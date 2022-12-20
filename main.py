#DALI
import requests

unfiltered_result = requests.get('https://api.datos.gob.mx/v1/calidadAire')

def get_last_value(pollutant):
    if unfiltered_result.status_code == 200:
        #print(unfiltered_result.json())
        results = unfiltered_result.json().get('results')
        for result in results:    
            res = result.get('stations')                
            filtered_result = res[0].get('measurements')                
            if len(filtered_result) == 0:
                #print("No hay datos")
                pass 
            else:
                if(filtered_result[0].get('pollutant')):
                    id_result = result.get('_id')
        
        return id_result
    elif unfiltered_result.status_code == 404:
        print('Not Encontrado. ')


def get_requested_values():
    if unfiltered_result.status_code == 200:
        #print(unfiltered_result.json())
        results = unfiltered_result.json().get('results')
        for result in results:    
            if (result.get('_id') == "58c780bf281e87010078f491"):
                res = result.get('stations')                
                filtered_result = res[0].get('measurements')    
                dic = { "value" : filtered_result[0].get("value"), "unit" : filtered_result[0].get("unit"), "pollutant" : filtered_result[0].get("pollutant") }
                return dic 
    
    elif unfiltered_result.status_code == 404:
        print('Not Encontrado. ')


if __name__ == '__main__':
    values = get_requested_values()
    print("================VALORES FILTRADOS====================")
    print(values)
    print("====================================================")
    id_value =get_last_value(values.get('pollutant'))
    print("=================ID FILTRADO===================")
    print(id_value)
    print("====================================================")
