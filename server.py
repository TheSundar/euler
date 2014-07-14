from twisted.internet import reactor, protocol
from twisted.protocols import basic
import time

def t():
    return "["+ time.strftime("%H:%M:%S") +"] "

class EchoProtocol(basic.LineReceiver):
    name = "Unnamed"

    def connectionMade(self):
        self.sendLine("Welcome, what is your name?")
        self.sendLine("")
        self.count = 0
        self.factory.clients.append(self)
        print t() + "+ Connection from: "+ self.transport.getPeer().host

    def connectionLost(self, reason):
        self.sendMsg("- %s left." % self.name)
        print t() + "- Connection lost: "+ self.name
        self.factory.clients.remove(self)

    def lineReceived(self, line):
        if line == 'quit':
            self.sendLine("Goodbye.")
            self.transport.loseConnection()
            return
        elif line == "userlist":
            self.chatters()
            return
        if not self.count:
            self.username(line)
        else:
            self.sendMsg(self.name +": " + line)

    def username(self, line):
        for x in self.factory.clients:
            if x.name == line:
                self.sendLine("This username is taken; please choose another")
                return

        self.name = line
        self.chatters()
        self.sendLine("Chat away!")
        self.sendLine("")
        self.count += 1
        self.sendMsg("+ %s joined." % self.name)
        print '%s~ %s is now known as %s' % (t(), self.transport.getPeer().host, self.name)

    def chatters(self):
        x = len(self.factory.clients) - 1
        s = 'is' if x == 1 else 'are'
        p = 'person' if x == 1 else 'people'
        self.sendLine("There %s %i %s connected:" % (s, x, p) )

        for client in self.factory.clients:
            if client is not self:
                self.sendLine(client.name)
        self.sendLine("")

    def sendMsg(self, message):
        for client in self.factory.clients:
            client.sendLine(t() + message)


class EchoServerFactory(protocol.ServerFactory):
    protocol  = EchoProtocol
    clients = []

if __name__ == "__main__":
    reactor.listenTCP(5001, EchoServerFactory())
    reactor.run()