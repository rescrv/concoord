from threading import RLock
from Connection import *
from utils import *

class Group():
    def __init__(self):
        self.members = []
        self.lock = RLock()

    def remove(self,peer):
        if peer in self.members:
            self.members.remove(peer)

    def add(self,peer):
        if self.ID == peer.ID:
            return
        for oldPeer in self.members:
            if oldPeer.ID == peer.ID:
                return
        self.members.append(peer)
        
    def broadcast(self,msg):
        print "DEBUG: broadcasting message.."
        replies = []
        for member in self.Group.members:
            reply = self.send_to_peer(member.addr,member.port,msg)
            replies.append(reply)
        return replies
    
    def send_to_peer(self,peer,msg):
        print "DEBUG: sending message to " + str(peer)
        reply = ""
        try:
            connection = Connection(peer.addr, peer.port)
            connection.send(msg)
            chunk = connection.receive()
            while (chunk != (None,None)):
                reply += chunk
                chunk = connection.receive()
            connection.close()
        except:
            print "Error in send_to_peer."
        return reply
            
    def __str__(self):
        output = ''
        for member in self.members:
            output += str(member)+'\n'
        return output