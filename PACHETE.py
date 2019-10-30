class SUBSCRIBE:
    def __init__(self, packetID, subscriptii):
        self.packetID = packetID
        self.subscriptii = subscriptii


class SUBPACK:
    def __init__(self, packetID, returnCode):
        self.packetID=packetID
        self.returnCode=returnCode


class PUBLISH:
    def __init__(self,topic,payload):
        self.topic=topic
        self.payload=payload


class CONNECT:
    def __init__(self, parola):
        self.parola = parola


class CONNACK:
    def __init__(self, flag_confirmare):
        self.flag_confirmare = flag_confirmare
