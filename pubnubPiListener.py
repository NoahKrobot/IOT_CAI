from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback
from gpiozero import LED
led2 = LED(2)
led3 = LED(3)
led4 = LED(4)
led17 = LED(17)
led22 = LED(22)
led27 = LED(27)
led10 = LED(10)

list =[]

list.append(led2)
list.append(led3)
list.append(led4)
list.append(led17)
list.append(led27)
list.append(led22)
list.append(led10)

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-a7c449e1-c9ca-484c-b992-2b146e8a0029"
pnconfig.user_id = "test_user"

pubnub = PubNub(pnconfig)

class MySubscribeCallback(SubscribeCallback):
    def message(self, pubnub, message):
        print(f"Received message: {message.message}")

        strengthPassed = message.message.get("text", "No text provided")
        strengthPassedInt = int(strengthPassed)
        turnOffPassed = message.message.get("turnOff", "No turnoff provided")
        
        print(strengthPassed)
        print(strengthPassedInt)
        print(turnOffPassed)

        if turnOffPassed.lower() == "false":
            if strengthPassedInt ==1:
                led2.on()
                led3.on()
                led4.on()
                led17.on()
                led22.on()
                led27.on()
                led10.on()
pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels("strength_ch").execute()

print("Listening")

