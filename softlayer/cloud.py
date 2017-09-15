'''
@author Ahmed Hassan Koshek
'''
import SoftLayer
from pprint import pprint as pp

class recovery:
    def cancel(self):
        self.mgr.cancel_instance(self.id)

    def getImageTemplateGUID(self, templateName):
	    mask = "mask[name,globalIdentifier]"
	    templates = self.client['SoftLayer_Account'].getBlockDeviceTemplateGroups(mask=mask)
	    for template in templates:
	        if template['name'] == templateName:
	            return template['globalIdentifier']

    def getObject(self):
        mask = '''
        	mask[
        		location,
        		datacenter,
        		startCpus,
        		maxMemory,
        		networkComponents.maxSpeed,
        		localDiskFlag,
        		blockDeviceTemplateGroup
        	]'''
        guest = self.client['SoftLayer_Virtual_Guest'].getObject(id=self.id, mask=mask)
        return guest

    def CreateObject(self):
        guest = self.getObject()
        guest['hostname'] = self.hostname
        guest['domain'] = self.domain
        guest['hourlyBillingFlag'] = true
        guest['networkComponents'] = [guest['networkComponents'][0]]
        guest['blockDeviceTemplateGroup'] = {'globalIdentifier': self.getImageTemplateGUID(self.imageName)}
        order_template = self.client['SoftLayer_Virtual_Guest'].createObject(guest)
        return order_template


    def recover(self):
        mask = "mask[hostname, status]"
        instance = self.mgr.get_instance(self.id, mask=mask)
        if(instance['status']['keyName'] != "DISCONNECTED"):
            return
        else:
            print("There is a failure in the machine .. RECOVERING ...")
            image = self.mgr.capture(self.id, self.imageName)
            Order = self.CreateObject()
            pp(Order)
            print("Created the new hourly server")




    def __init__(self, client, id, imageName, hostname, domain):
        self.client = client
        self.mgr = SoftLayer.VSManager(self.client)
        self.id = id
        self.imageName = imageName
        self.hostname = hostname #hostname and domain for the temp servers
        self.doamin = domain
