import { Component } from '@angular/core';
import firebase from 'firebase';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  constructor() {
    const firebaseConfig = {
        apiKey: "AIzaSyDnHHKSCCcsXpyjxPBtSh-nQ7aZfGDIYu8",
        authDomain: "firstproject-aa4fd.firebaseapp.com",
        databaseURL: "https://firstproject-aa4fd-default-rtdb.europe-west1.firebasedatabase.app",
        projectId: "firstproject-aa4fd",
        storageBucket: "firstproject-aa4fd.appspot.com",
        messagingSenderId: "998528775360",
        appId: "1:998528775360:web:836f5754e3598d13876925",
        measurementId: "G-V6LL8N4N0V"
      };
      firebase.initializeApp(firebaseConfig);
  }
}
