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
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def message(self,pubnub, message_object):
            print(f'Incoming message_object: {message_object} Message: {message_object.message}')

            if message_object.channel == CHANNELS['BLOCK']:
                block = message_object.message
                potential_chain = self.blockchain.chain[:len(self.blockchain.chain)]
                potential_chain.append(block)

                try:
                    self.blockchain.replace_chain(potential_chain)
                    print(' Successfully replaced the local chain')
                except Exception as e:
                    print(f'Did not replace chain: {e}')


class PubSub():
    """
    Handles the publish and subscribe layer of the application.
    Provides communication between the nodes of the blockchain network
    """
    def __init__(self, blockchain):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain))

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