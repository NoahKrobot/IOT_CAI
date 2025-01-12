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

# listLeds =[]

# listLeds.append(led2)
# listLeds.append(led3)
# listLeds.append(led4)
# listLeds.append(led17)
# listLeds.append(led27)
# listLeds.append(led22)
# listLeds.append(led10)

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-a7c449e1-c9ca-484c-b992-2b146e8a0029"
pnconfig.user_id = "noahid"

pubnub = PubNub(pnconfig)
print("*** Listening ***")

class ReceiveMsg(SubscribeCallback):
    def message(self, pubnub, message):
        # print(f"Message: {message.message}")

        strengthPassed = message.message.get("text", "No text")
        strengthPassedInt = int(strengthPassed)
        turnOffPassed = message.message.get("turnOff", "No text")
        
        print(strengthPassed)
        print(strengthPassedInt)
        print(turnOffPassed)

        if turnOffPassed.lower() == "false":
            if strengthPassedInt ==1:
                led2.on()
                led3.off()
                led4.off()
                led17.off()
                led27.off()
                led22.off()
                led10.off()
            if strengthPassedInt ==2:
                led2.on()
                led3.on()
                led4.off()
                led17.off()
                led27.off()
                led22.off()
                led10.off()
            if strengthPassedInt ==3:
                led2.on()
                led3.on()
                led4.on()
                led17.off()
                led27.off()
                led22.off()
                led10.off()
            if strengthPassedInt ==4:
                led2.on()
                led3.on()
                led4.on()
                led17.on()
                led27.off()
                led22.off()
                led10.off()
            if strengthPassedInt ==5:
                led2.on()
                led3.on()
                led4.on()
                led17.on()
                led27.on()
                led22.off()
                led10.off()
            if strengthPassedInt ==6:
                led2.on()
                led3.on()
                led4.on()
                led17.on()
                led27.on()
                led22.on()
                led10.off()
            if strengthPassedInt ==7:
                led2.on()
                led3.on()
                led4.on()
                led17.on()
                led27.on()
                led22.on()
                led10.on()
        else:
                led2.off()
                led3.off()
                led4.off()
                led17.off()
                led27.off()
                led22.off()
                led10.off()
pubnub.add_listener(ReceiveMsg())
pubnub.subscribe().channels("strength_ch").execute()



