from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-a7c449e1-c9ca-484c-b992-2b146e8a0029"
pnconfig.user_id = "test_user"

pubnub = PubNub(pnconfig)

class MySubscribeCallback(SubscribeCallback):
    def message(self, pubnub, message):
        print(f"msg: {message.message}")
    
pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels("strength_ch").execute()

print("Listening...")

