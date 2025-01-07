const chat = await Chat.init({
    publishKey: "pub-c-6c61f0f4-a610-4bc4-a4b8-72c7a57d5fd1",
    subscribeKey: "sub-c-a7c449e1-c9ca-484c-b992-2b146e8a0029",
    userId,
    typingTimeout: 2000,
  })
  