# -*- coding: utf-8 -*-
"""Module with Kyco Events"""

from kyco.utils import now


#######################
# Base Events Classes #
#######################

class KycoEvent(object):
    """Base Event class

    The event data will be passed on the content attribute, which should be a
    dictionary.

    Args:
        content (dict): Dictionary with all event informations
    """
    context = 'None'

    def __init__(self, dpid=None, content=None, connection_id=None,
                 timestamp=now()):
        self.content = content if content is not None else {}
        self.connection_id = connection_id
        self.dpid = dpid
        self.timestamp = timestamp


class KycoCoreEvent(KycoEvent):
    """Kyco Core Event base class.

    Events generated by Kyco or any Core NApps
    """
    context = 'core'


class KycoMsgEvent(KycoEvent):
    """Base class for all Events related to OpenFlow Messages"""
    context = 'message'


class KycoAppEvent(KycoEvent):
    """Base class for all Events generated to/by Apps that are not OpenFlow
    Messages"""
    context = 'apps'

    def __init__(self, dpid=None, content=None,
                 timestamp=now()):
        super().__init__(dpid, content, None, timestamp)


class KycoRawEvent(KycoCoreEvent):
    """Kyco Event generated by incoming packets from the network.

    This needs to be handled and a new event will be generated by the handler.
    Mainly this will have an OpenFlowMessage or will be an event about a new
    incoming TCP connection.
    """
    pass


#########################
# Core Generated Events #
#########################


class KycoConnectionLost(KycoRawEvent):
    """A connection was lost"""
    def __init__(self, dpid=None, connection_id=None, timestamp=now()):
        if dpid is None and connection_id is None:
            raise Exception('The dpid or the connection must be passed')
        super().__init__(dpid, None, connection_id, timestamp)


class KycoNewConnection(KycoRawEvent):
    """A new Connection was stabilished"""
    def __init__(self, connection_id, content, timestamp=now()):
        super().__init__(None, content, connection_id, timestamp)


class KycoRawOpenFlowMessage(KycoRawEvent):
    """New OpenFlowMessage received

    This event contains the header of the message and also the body in binary
    format, that still needs to be unpacked."""
    pass


class KycoRawError(KycoRawEvent):
    """This event is just a wrapper to KycoErro event"""
    pass


class KycoShutdownEvent(KycoEvent):
    """Dispatched by the controller to announce that it is shuting down"""
    context = 'core'

    def __init__(self):
        super().__init__(None, {}, None, now())


######################################
# Events to/from NApps communication #
######################################


class KycoSwitchUp(KycoAppEvent):
    """A connection with a switch was stabilished (After handshake)"""
    pass


class KycoSwitchDown(KycoAppEvent):
    """A connection with a switch was lost"""
    pass


class KycoAppInstalled(KycoAppEvent):
    pass


class KycoAppLoaded(KycoAppEvent):
    pass


class KycoAppUninstalled(KycoAppEvent):
    pass


class KycoAppUnloaded(KycoAppEvent):
    pass


class KycoServerDown(KycoAppEvent):
    pass


class KycoError(KycoAppEvent):
    pass


##########################
# OpenFlowMessage events #
##########################


class KycoMessageIn(KycoMsgEvent):
    pass


class KycoMessageOut(KycoMsgEvent):
    pass


class KycoMessageInEchoRequest(KycoMessageIn):
    pass


class KycoMessageOutEchoReply(KycoMessageOut):
    pass


class KycoMessageOutEchoRequest(KycoMessageOut):
    pass


class KycoMessageInEchoReply(KycoMessageIn):
    pass


class KycoMessageInHello(KycoMessageIn):
    pass


class KycoMessageOutHello(KycoMessageOut):
    pass


class KycoMessageOutFeaturesRequest(KycoMessageOut):
    pass


class KycoMessageInFeaturesReply(KycoMessageIn):
    pass


class KycoMessageOutSetConfig(KycoMessageOut):
    pass
