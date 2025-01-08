import { initializeApp } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-app.js";
import { getFirestore, collection, addDoc } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyCYArcypqqY73wFtwGrzlegjyhkhRiuzuM",
  authDomain: "lightbook-24211.firebaseapp.com",
  projectId: "lightbook-24211",
  storageBucket: "lightbook-24211.appspot.com",
  messagingSenderId: "245779430190",
  appId: "1:245779430190:web:bdb631444719512e1b58bf",
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app); 

document.getElementById("letThereBeLightButton").onclick = async function () {
  const strength = document.getElementById("strengthSlider").value;
  const time = new Date().toISOString();
    const strengthCollection = collection(db, "pushed_strength");

  const formData = {
    strength: strength,
    time: time,
  };

  try {
    await addDoc(strengthCollection, formData);
    console.log("to firebase:", formData);
  } catch (e) {
    console.error('err:',e);
  }
};