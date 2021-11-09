from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = ''
pnconfig.publish_key = ''
pubnub = PubNub(pnconfig)

pubnub.subscribe().channels([]).execute()

class Listener(SubscribeCallback):
    def message(self,pubnub, message_object):
            print(f'Incoming message_object: {message_object}')

pubnub.add_listener()

pubnub.publish().channel().message({'foo':'bar'}).sync()

if __name__ == '__main__':
    main()