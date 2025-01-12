let pubnub;

async function setupPubNub(turnOff) {
  // console.log('test')
  const strengthValue = document.getElementById("strengthSlider").value;

  pubnub = new PubNub({
    publishKey: "pub-c-6c61f0f4-a610-4bc4-a4b8-72c7a57d5fd1",
    subscribeKey: "sub-c-a7c449e1-c9ca-484c-b992-2b146e8a0029",
    userId: "noah_id",
  });

  var messageStr
  if(turnOff){
     messageStr = {                  
      text: strengthValue,  
      timestamp: new Date().toISOString(), 
      turnOff: "true"
    };
  }else{
     messageStr = {                  
      text: strengthValue,  
      timestamp: new Date().toISOString(), 
      turnOff: "false"
    };
  }

  pubnub.publish(
    {
      channel: "strength_ch",
      message: messageStr,
    },
    function (status, response) {
      if (status.error) {
        console.error("Error:", status);
      } else {
        console.log("Message sent!");
      }
    }
  );
}
