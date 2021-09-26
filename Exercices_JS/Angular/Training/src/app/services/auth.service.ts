import { Injectable } from '@angular/core';

@Injectable({
    providedIn: 'root'
})
export class AuthService {
    isAuth = false;
    userId: number = -1;

    constructor() { }

    signIn(id: number) {
        this.isAuth = true;
        this.userId = +id;
        console.log('userId from authService: ' +this.userId);
    }

    signOut() {
        this.isAuth = false;
        this.userId = -1;
    }


}
