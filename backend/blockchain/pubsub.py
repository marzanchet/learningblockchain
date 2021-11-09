import time
from typing import ChainMap

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = ''
pnconfig.publish_key = ''

CHANNELS = {
    'TEST' : 'TEST',
    'BLOCK' : 'BLOCK'
}

class Listener(SubscribeCallback):
    def message(self,pubnub, message_object):
            print(f'Incoming message_object: {message_object} Message: {message_object.message}')


class PubSub():
    """
    Handles the publish and subscribe layer of the application.
    Provides communication between the nodes of the blockchain network
    """
    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, message):
        """
        Publish the message object to the channel.
        """
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self, block):
        """
        Broadcast a block object to all nodes.
        """
        self.publish(CHANNELS['BLOCK'], block.to_json())

def main():
    pubsub = PubSub()

    time.sleep(1)

    pubnub.publish(CHANNELS['TEST'], {'foo':'bar'})

if __name__ == '__main__':
    main()