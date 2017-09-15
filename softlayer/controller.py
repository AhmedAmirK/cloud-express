'''
@author Ahmed Hassan Koshek
'''
#import Cloud as cloud
import SoftLayer
from pprint import pprint as pp
import math
import threading
import clients
import cloud
import connection


class cloudThread(threading.Thread):
    def __init__(self, users):
        threading.Thread.__init__(self)
        self.users = users

    def run(self):
        for user in self.users:
            client = SoftLayer.Client(
                username=user['username'],
                api_key=user['key']
            )
            guest = clients.Guest(client)
            i = 0
            for id in user.ids:
                VirtualGuest = cloud.recovery(client, id, user.imageNames[i], user.hostname[i], user.domain[i])
                VirtualGuest.recover()
                i = i + 1
                print("Done")


class controller:
    def __init__(self):
        db = connection.connect()
        db.start_connection()

        threads = []
        numThreads = math.ceil(db.count/10)

        iFirst = 0
        iLast = 9
        for i in range(int(numThreads)):
            if(i < int(numThread))::
                thread = cloudThread(db.users[iFirst:iLast])
            else:
                thread = cloudThread(db.users[iFirst:db.count - 1])
            thread.start()
            threads.append(thread)
            iFirst = iFirst + 10
            iLast = iLast + 10

        for t in threads:
            t.join()

        db.close_connection()




    #spaces
