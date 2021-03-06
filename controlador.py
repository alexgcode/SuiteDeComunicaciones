import requests
import time
from get_glpi_data2 import obtener_ticket
from get_glpi_data2 import obtener_seguimientos
from get_glpi_data2 import obtener_todos_tickets
from get_glpi_data2 import obtener_updates
from send_sms import send_sms


#r0 = requests.get('http://x.x.x.x:5000/updates')
#data0 = r0.json()
data0 = obtener_updates()
last_ticket = data0[-1]


#----------------------metodos usados para consulta telegram--------------------------#





#----------------------metodos usados en este modulo----------------------------------#
def get_status(id_status):
    #ticket['status']
    switcher = {
        1: "Nuevos",
        2: "En curso (asignada)",
        3: "En curso (planificada)",
        4: "En espera",
        5: "Resuelto",
        6: "Cerrado"
    }
    return switcher.get(id_status, "invalid argument")



def follow_text(followup):
    last_follow = "error en follow_text"
    for n in range(0, len(followup)):
        last_follow = followup[n]['content']

    return last_follow

def last_follow(followups):
    last_follow = None
    for n in range(0, len(followups)):
        last_follow = followups[n]

    return last_follow

def find_data_by_id(data, id):
    data0 = None
    for n in range(0, len(data)):
        if data[n][0] == id:
            data0 = data[n]
            return data0
    return data0
#-------------------------------------------------------------------------------

#la primera obtencion de requerimientos
##seguimiento1 = follow_text(obtener_seguimientos())
seguimiento1 = last_follow(obtener_seguimientos())
tickets1 = obtener_todos_tickets()


telefono = "error en telefono"
#loop principal
#imprime el id y el nombre del ultimo ticket
while True:
    #r = requests.get('http://192.168.111.145:5000/updates')
    #data = r.json()
    data = obtener_updates()
    if(last_ticket != data[-1]):
        last_ticket = data[-1] #ultimo ticket con eleccion de medio de comunicacion(id_ticket, medio, telefono)
        ticket = obtener_ticket(last_ticket[0]) #ticket id

        print(last_ticket[0]) #imprime del id del ultimo ticket
        print(ticket['name']) #imprime nombre del ticket
        print("telefono: " + last_ticket[2])
        if(last_ticket[1] == 2):
            print("su medio de aviso es SMS")
            medio = 2

        print("----------")

    else:
        print("son iguales")

    
    #imprime el ultimo seguimiento hecho a cualquier ticket
    '''
    followup = obtener_seguimientos()
    seguimiento2 = follow_text(followup)
    if(seguimiento1 != seguimiento2):
        print(seguimiento2)
        seguimiento1 = seguimiento2
    '''
    #detecta y envia seguimientos por sms
    followups = obtener_seguimientos()
    seguimiento2 = last_follow(followups)
    if(seguimiento1['id'] != seguimiento2['id']):
            
        if(find_data_by_id(data, seguimiento2['tickets_id'])[1] == 2 and find_data_by_id(data, seguimiento2['tickets_id'])[2] != None):
            print("medio del ticket: " + str(find_data_by_id(data, seguimiento2['tickets_id'])[1]))
            print("telefono al que se envia el seguimiento: " + str(find_data_by_id(data, seguimiento2['tickets_id'])[2]))
            print("seguimiento2 --> tickets_id: " + str(seguimiento2['tickets_id']))
            #print(find_data_by_id(data, seguimiento2['tickets_id']))
            print(seguimiento2['content'])
            send_sms(find_data_by_id(data, seguimiento2['tickets_id'])[2], str("seguimiento del ticket "+str(seguimiento2['tickets_id']) +": "+ seguimiento2['content']))
            print("enviado por sms")

        seguimiento1 = seguimiento2
    

    #detecta y envia el cambio de estado
    tickets2 = obtener_todos_tickets() 
    if len(tickets1) < len(tickets2):
            print("se creo un nuevo ticket")
    else:
        for n in range(0,len(tickets2)):
            if tickets1[n]['status'] != tickets2[n]['status']:
                status = get_status(tickets2[n]['status'])
                if(data[n-1][1] == 2): #valida si se envia por sms
                    print("telefono al que se envia el aviso de cambio de estado: " + str(data[n-1][2]))
                    send_sms(data[n-1][2],str("El estado de atención de su ticket "+str(data[n-1][0])+" cambio a: " + status))
                    print("se envió mensaje por sms de cambio de estado del ticket nro " + str(n+1) + ". Nuevo estado es: " + status)
                
                
        
    tickets1 = tickets2

    time.sleep(5)
