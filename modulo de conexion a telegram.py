from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import logging
from get_glpi_data2 import obtener_ticket
from get_glpi_data2 import obtener_grupos
import json
import re

updater = Updater(token='')

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#--------------------------otros metodos---------------------------------
def get_time_to_resolve(id_ticket):
    print("nro de ticket solicitado: " + str(id_ticket))
    ticket = obtener_ticket(id_ticket)
    if ticket['time_to_resolve'] == None:
        print("No se a asignado fecha a completar")
        return "no se asigno fecha a completar"
    else:
        print("fecha a completarse: " + ticket['time_to_resolve'])
        return ticket['time_to_resolve']


def get_creation_date(id_ticket):
    print("nro de ticket solicitado: " + str(id_ticket))
    ticket = obtener_ticket(id_ticket)
    print("fecha de creación: " + ticket['date'])
    return ticket['date']

def get_group_ticket(id_ticket):
    print("nro de ticket solicitado: " + str(id_ticket))
    groups = obtener_grupos()
    group_ticket = "no hay ningun grupo asignado"
    for item in groups:
        print(item[0])
        if int(item[0]) == int(id_ticket):
            print("se seleccionó el ticket nro: " + str(item[0]))
            group_ticket = get_group(item[1])
    
    return group_ticket


def get_group(id_group):
    switcher = {
        1: "Servicedesk",
        2: "STI"
    }
    return switcher.get(id_group, "invalid argument")

#--------------------------------------
def get_ticket_status(id_ticket):
    print("nro de ticket solicitado: " + str(id_ticket))
    ticket = obtener_ticket(id_ticket)
    print("id de estado: " + str(ticket['status']))
    estado = get_status(ticket['status'])
    return estado

def get_status(id_status):
    #ticket['status']
    switcher = {
        1: "Nuevo",
        2: "En curso (asignada)",
        3: "En curso (planificada)",
        4: "En espera",
        5: "Resuelto",
        6: "Cerrado"
    }
    return switcher.get(id_status, "invalid argument")

#----------------------------------------------------------------------

def echo(bot, update):
    chatID = update.message.chat_id
    chatText = update.message.text	#get message from user
    
    if chatText == 'menu':
        bot.send_message(chat_id=chatID, text="Para consultar datos sobre un ticket haga lo siguiente \n1. Para consultar el estado de un ticket escriba: estado nro_del_ticket \n2. Para consultar la fecha de creacion de un ticket escriba: creacion nro_del_ticket \n3. Para consultar la fecha de finalización de un ticket escriba: termino nro_del_ticket \n4. Para consultar el área que esta atendiendo un ticket escriba: area nro_del_ticket")
        
    if 'estado' in chatText:  #estado nro_del_ticket
        nro = re.findall(r'\d+', chatText)
        print(nro)
        print(nro[0])
        respuesta = get_ticket_status(nro[0])
        bot.send_message(chat_id=chatID, text=respuesta)
        
    if 'creacion' in chatText:
        nro = re.findall(r'\d+', chatText)
        print(nro)
        print(nro[0])
        respuesta = get_creation_date(nro[0])
        bot.send_message(chat_id=chatID, text=respuesta)

    if 'termino' in chatText:
        nro = re.findall(r'\d+', chatText)
        print(nro)
        print(nro[0])
        respuesta = get_time_to_resolve(nro[0])
        bot.send_message(chat_id=chatID, text=respuesta)

    if 'area' in chatText:
        nro = re.findall(r'\d+', chatText)
        print(nro)
        print(nro[0])
        respuesta = get_group_ticket(nro[0])
        bot.send_message(chat_id=chatID, text=respuesta)
            
'''
    elif chatText.isdigit():
        respuesta = obtener_nombre(chatText)
        bot.send_message(chat_id=chatID, text=respuesta)
    else:
        bot.send_message(chat_id=chatID, text='porfavor ingrese un número')

    #bot.send_message(chat_id=chatID, text='pruebas 3')

'''
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)



updater.start_polling()
