import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { User } from '../models/user.model';
import { UserService } from '../services/user.service';
import { AuthService } from '../services/auth.service';

@Component({
    selector: 'app-user-list',
    templateUrl: './user-list.component.html',
    styleUrls: ['./user-list.component.scss']
})
export class UserListComponent implements OnInit, OnDestroy {
    users!: User[];
    userSubscription!: Subscription;
    userId!: number;

    constructor(private userService: UserService,
                private authService: AuthService) { }

    ngOnInit() {
        this.userService.getAllUsers();
        this.userSubscription = this.userService.userSubject
            .subscribe((users: User[]) =>  {
            this.users = users;
        });
        this.userId = this.authService.userId;
        console.log(+this.userId);
    }

    onDelete(){
        console.log('userId: ' + this.userId);
        this.userService.deleteUser(this.userId);
    }


    ngOnDestroy() {
        this.userSubscription.unsubscribe();
    }

}
