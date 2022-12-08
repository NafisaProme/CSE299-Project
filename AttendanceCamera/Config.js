import firebase from "firebase/compat/app";
import 'firebase/compat/auth';
import 'firebase/compat/firestore';
import 'firebase/compat/storage';

const firebaseConfig =
{
    apiKey: "AIzaSyC6lEwU-QT4toNNEvWs63jsnKSaIIFuvvo",
    authDomain: "attendancecamera.firebaseapp.com",
    projectId: "attendancecamera",
    storageBucket: "attendancecamera.appspot.com",
    messagingSenderId: "338003251006",
    appId: "1:338003251006:web:ea222a928384aaa255266f",
    measurementId: "G-796BC5GJV1"
};

if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
}

export { firebase };