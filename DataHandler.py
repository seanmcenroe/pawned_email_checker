from zeep import Client
from zeep import Transport
import time


class DataHandler(object):

    @staticmethod
    def grab_url():
        url = "http://pointer_to_service/dbaService.svc"
        
        return url

    @staticmethod
    def grab_xml():
        dbaXML = ""
        dbaXML = "<soapenv:Envelope xmlns:soapenv='http://schemas.xmlsoap.org/soap/envelope/' xmlns:tem='http://tempuri.org/' xmlns:dbas='http://schemas.datacontract.org/2004/07/dbaService'>"
        dbaXML += "<soapenv:Header/>"
        dbaXML += "<soapenv:Body>"
        dbaXML += "<tem:ExecuteQuery>"
        dbaXML += "  <tem:composite>"
        dbaXML += "     <dbas:Database>[DATABASE HERE]</dbas:Database>"
        dbaXML += "     <dbas:SQL>[SQL HERE]</dbas:SQL>"
        dbaXML += "     <dbas:source>"
        dbaXML += "        <dbas:callingClass>pyReciever</dbas:callingClass>"
        dbaXML += "        <dbas:callingMethod>callback</dbas:callingMethod>"
        dbaXML += "        <dbas:subsystem>python</dbas:subsystem>"
        dbaXML += "     </dbas:source>"
        dbaXML += "  </tem:composite>"
        dbaXML += "</tem:ExecuteQuery>"
        dbaXML += "</soapenv:Body>"
        dbaXML += "</soapenv:Envelope>"
        return dbaXML

    @classmethod
    def executeSQL(cls, sql, database):
        my_url = cls.grab_url()
        xml = cls.grab_xml()
        xml = xml.replace("[DATABASE HERE]", database)
        xml = xml.replace("[SQL HERE]",sql)
        headers = {'content-type': 'text/xml;charset=UTF-8', 'SOAPAction': 'http://tempuri.org/IdbaService/ExecuteQuery'}
        resp = Transport()
        resp1 = resp.post(my_url, xml, headers)
        return resp1
        return result

    @classmethod
    def check_email(cls,email):
        pawned_url = "http://haveibeenpwned.com/api/v2/breachedaccount/" + email
        headers = {'content-type': 'text/json;charset=UTF-8','User-Agent':'hillgate-email-checker-v1' }
        resp = Transport()
        time.sleep(3)
        result = ""
        try:
            resp1 = resp.get(pawned_url, "", headers)
            if resp1.status_code == 429:
                #need to wait before trying again
                time.sleep(respl.status)
                result = "WAIT"
            if ((resp1.status_code == 200) or (resp1.status_code == 404)):
                if len(resp1._content) == 0:
                    result = "NOT FOUND"
                else:
                    result = "PAWNED"

        except:
            result = "ERROR"
        return result
