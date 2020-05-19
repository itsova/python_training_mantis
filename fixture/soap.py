from suds.client import Client
from suds import WebFault

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def project_lists(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        try:
            list = client.service.mc_projects_get_user_accessible(username, password)
            return list
        except WebFault:
            list = []
            return list
        



