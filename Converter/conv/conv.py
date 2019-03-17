import urllib.request
import datetime
from xml.etree import ElementTree as et

def get_values(arg1 , arg2):
    diction_id = {
        "USD" : "R01235",
        "EUR" : "R01239",
    }
    if "RUB" in [arg1, arg2]:
        if arg1 == "RUB":
            val_arg1 = 1 
        if arg2 == "RUB":
            val_arg2 = 1 
    values = et.parse(urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp"))
    id_a1, id_a2 = diction_id.get(arg1), diction_id.get(arg2)
    for line in values.findall('Valute') :
        id = line.get('ID')
        if id in [id_a1, id_a2]:
            if id_a1 == id:
                val_arg1 = line.find('Value').text
                val_arg1 = val_arg1.replace(",",".")
                val_arg1 = float(val_arg1)
            if id_a2 == id:
                val_arg2 = line.find('Value').text
                val_arg2 = val_arg2.replace(",",".")
                val_arg2 = float(val_arg2)
    today = datetime.date.today()
    return val_arg1, val_arg2, today
