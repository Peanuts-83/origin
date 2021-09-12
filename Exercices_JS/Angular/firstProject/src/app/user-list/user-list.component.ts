import { Component, OnInit, OnDestroy } from '@angular/core';
import { User } from '../models/User.model';
import { UserService } from '../services/user.service';
import { Subscription } from 'rxjs';
import { AuthService } from '../services/auth.service';
import { Router } from '@angular/router';
import { AuthComponent } from '../auth/auth.component';
import { MethodCall } from '@angular/compiler';

@Component({
  providers:[AuthComponent],
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.scss']
})
export class UserListComponent implements OnInit {

  users!: User[];
  userSubscription!: Subscription;

  constructor(private userService: UserService, private authService: AuthService, private router: Router, private authComponent: AuthComponent) { }

  ngOnInit() {
    this.userSubscription = this.userService.userSubject.subscribe(
                            (users: User[]) => {
                              this.users = users;
                            });
    this.userService.emitUsers();
  }

  ngOnDestroy() {
    this.userSubscription.unsubscribe();
  }

  newUser() {
    this.authComponent.newUser();
  }
}
