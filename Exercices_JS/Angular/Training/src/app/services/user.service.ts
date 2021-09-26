import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Subject } from 'rxjs';
import { User } from '../models/user.model';

@Injectable()
export class UserService{

    userSubject = new Subject<User[]>();
    private users: User[] = [
        new User(0,'totolehero','pass12345','pass12345','tom','zaz','qs@erert.fr','beer',['hobbie1','hoobbie2','hobbie3'])
    ];
    usersLength = this.users.length;

    constructor(private httpClient: HttpClient,
                private router: Router) {}


    saveUsers() {
        this.users.forEach(
            (user, index) => {
                user.userId = index;
            }
        );
        this.httpClient
            .put('https://firstproject-aa4fd-default-rtdb.europe-west1.firebasedatabase.app/users.json', this.users)
            .subscribe(
                () => {
                    console.log('UserList saved!');
                    this.router.navigate(['/users']);
                },
                (error) => console.log('Erreur de sauvegarde de la liste utilisateurs: ' +error)
            )
    }



    getAllUsers() {
        this.httpClient
            .get<any[]>('https://firstproject-aa4fd-default-rtdb.europe-west1.firebasedatabase.app/users.json')
            .subscribe(
                (data) => {
                    this.users = data;
                    this.usersLength = this.users.length;
                    this.emitUsers();
                    /* return this.users; */
                },
                (error) => {
                    console.log("Erreur d'import des profils utilisateur: " + error);
                }
            )
    }

    getUser(login: string, password: string) {
        this.httpClient
            .get<any[]>('https://firstproject-aa4fd-default-rtdb.europe-west1.firebasedatabase.app/users.json')
            .subscribe(
                (data) => {
                    this.users = data;
                    const user = this.users.find(
                        (user) => {
                            console.log(login === user.login);
                            console.log(password === user.password);
                            return user.login === login;
                        });
                    console.log(user);
                    if (user !== undefined && user.password === password) {
                        console.log('You are Logged In');
                        console.log('Id from userService: ' +user.userId)
                        return +user.userId;
                    } else {
                        console.log('Utilisateur non trouvé');
                    }
                    return -1;
                },
                (error) => {
                    console.log("Erreur d'accès à l'utilisateur: " + error);
                    return -1;
                }
            )
    }

    deleteUser(userId: number) {
        /* this.users.splice(userId, 1); */
        this.emitUsers();
        this.saveUsers();
    }


    emitUsers() {
        this.userSubject.next(this.users);
    }

    addUser(user: User) {
        this.users.push(user);
        this.emitUsers();
        this.saveUsers();
    }
}
