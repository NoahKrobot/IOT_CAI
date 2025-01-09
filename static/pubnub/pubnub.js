let pubnub;

async function setupPubNub() {
  console.log('test')
  const strengthValue = document.getElementById("strengthSlider").value;

  // Initialize PubNub
  pubnub = new PubNub({
    publishKey: "pub-c-6c61f0f4-a610-4bc4-a4b8-72c7a57d5fd1",
    subscribeKey: "sub-c-a7c449e1-c9ca-484c-b992-2b146e8a0029",
    userId: "noah_id",
  });

  const messageStr = {                  
    text: strengthValue,  
    timestamp: new Date().toISOString(), 
    turnOff: "false"
  };

  // Publish the message
  pubnub.publish(
    {
      channel: "strength_ch",
      message: messageStr,
    },
    function (status, response) {
      if (status.error) {
        console.error("Error publishing message:", status);
      } else {
        console.log("Message sent successfully:", response);
      }
    }
  );
}
