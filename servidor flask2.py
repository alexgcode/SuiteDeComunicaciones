#consulta a la bd glpi y extrae los datos de la tabla ticketmeidodecomunicacion..
import mysql.connector



def get_tickets():
    cnx = mysql.connector.connect(user='admin', 
                                  password='admin',
                                  host='127.0.0.1',
                                  database='glpi')

    cursor = cnx.cursor()

    query = "SELECT items_id, plugin_fields_telegramfielddropdowns_id FROM glpi_plugin_fields_ticketmediodecomunicacion1s"
    query2 = "SELECT items_id, plugin_fields_telegramfielddropdowns_id, numerodetelefonofield FROM glpi_plugin_fields_ticketmediodecomunicacion1s"
    
    cursor.execute(query)

    result = cursor.fetchall()
    cnx.close()
    
    return result



def get_tickets22():
    cnx = mysql.connector.connect(user='admin', 
                                  password='admin',
                                  host='127.0.0.1',
                                  database='glpi')

    cursor = cnx.cursor()

    
    query = "SELECT items_id, plugin_fields_telegramfielddropdowns_id, numerodetelefonofield FROM glpi_plugin_fields_ticketmediodecomunicacion1s"
    
    cursor.execute(query)

    result = cursor.fetchall()
    cnx.close()
    
    return result

def get_groups():
    cnx = mysql.connector.connect(user='admin', 
                                  password='admin',
                                  host='127.0.0.1',
                                  database='glpi')

    cursor = cnx.cursor()
    query = "SELECT tickets_id, groups_id from glpi_groups_tickets"
    cursor.execute(query)

    result = cursor.fetchall()
    cnx.close()
    
    return result



