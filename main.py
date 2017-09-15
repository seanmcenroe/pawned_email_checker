import DataHandler
from xml.etree.ElementTree import XML


d = DataHandler.DataHandler()
r = d.executeSQL("select * from users", "Planner")

tree = XML(r.text)
nodes = tree.find(".//DocumentElement")
for node in nodes:
    if node.tag == "DataResults":
        for elems in node:
            if elems.tag == "user_principal_name":
                mail = elems.text
                if mail:
                    resp = d.check_email(mail)
                    print(resp + ': ' + mail)
                    if resp == "WAIT":
                        resp = d.check_email(mail)
                        print(resp + ': ' + mail)
