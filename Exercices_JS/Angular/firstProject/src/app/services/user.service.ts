import { User } from "../models/User.model";
import { Subject } from "rxjs";

export class UserService {
    
    userSubject = new Subject<User[]>();

    emitUsers() {
        this.userSubject.next(this.users.slice());
    }

    addUsers(user: User) {
        this.users.push(user);
        this.emitUsers();
    }

    private users: User[] = [
        new User('Tom', 'Ranq', 'toto@me.io', 'beer', ['cook','sport','code', 'read'])
    ];
}