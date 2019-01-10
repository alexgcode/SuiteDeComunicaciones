import requests


def obtener_seguimientos():
    r = requests.get('http://192.168.111.148/glpi/apirest.php/TicketFollowup?session_token=4e4kd82peohmudl1q63dsfhes2&app_token=yGmpIbYNfCFMVFqoTjkhcW9v1Vc800HpiAXsIzH1&range=0-999')
    rawData = r.json()
    return rawData


def obtener_ticket(id_ticket):
    r = requests.get('http://192.168.111.148/glpi/apirest.php/Ticket/%s?session_token=4e4kd82peohmudl1q63dsfhes2&app_token=yGmpIbYNfCFMVFqoTjkhcW9v1Vc800HpiAXsIzH1' % id_ticket)
    rawData = r.json()
    return rawData

def obtener_todos_tickets():
    r = requests.get('http://192.168.111.148/glpi/apirest.php/Ticket?session_token=4e4kd82peohmudl1q63dsfhes2&app_token=yGmpIbYNfCFMVFqoTjkhcW9v1Vc800HpiAXsIzH1&range=0-999')
    rawData = r.json()
    return rawData

def obtener_updates():
    r = requests.get('http://192.168.111.148:5000/updates22')
    rawData = r.json()
    return rawData

def obtener_grupos():
    r = requests.get('http://192.168.111.148:5000/groups')
    rawData = r.json()
    return rawData

