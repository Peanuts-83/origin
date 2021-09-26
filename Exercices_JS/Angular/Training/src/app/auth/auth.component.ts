import { Component, OnInit } from '@angular/core';
import { AbstractControl, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { CustomValidators } from '../custom-validators';
import { AuthService } from '../services/auth.service';
import { UserService } from '../services/user.service';

@Component({
    selector: 'app-auth',
    templateUrl: './auth.component.html',
    styleUrls: ['./auth.component.scss']
})
export class AuthComponent implements OnInit {
    authStatus!: boolean;
    authForm!: FormGroup;
    userId: number = -1;
    submitted = false;

    constructor(private authService: AuthService,
        private formBuilder: FormBuilder,
        private userService: UserService,
        private router: Router) { }

    ngOnInit(): void {
        this.authStatus = this.authService.isAuth;
        this.initForm();
    }

    initForm() {
        this.authForm = this.formBuilder.group({
            login: ['', Validators.required],
            password: ['', Validators.required]
        }/* ,{
            validators: [
                CustomValidators.idCheck('login','password')
            ]
        } */
        );
    }

    onSignIn() {
        this.submitted = true;
        if (this.authForm.invalid) { return; }
        const formVal = this.authForm.value;
        console.log(formVal.login, formVal.password);
        const getUserId = async () => {
            const userId = +this.userService.getUser(formVal.login, formVal.password);
        }
        getUserId().then(
            (data) => {
                this.userId = +data;
                console.log('userId from authComp: ' + this.userId);
                if (this.userId === undefined || this.userId < 0) {
                    alert('Mot de passe incorrect!');
                    return;
                }
                this.authService.signIn(this.userId);
                this.submitted = false;
                this.router.navigate(['appareils']);
            }
            )


    }

    get u(): { [key: string]: AbstractControl } {
        return this.authForm.controls;
    }


    onSignOut() {
        console.log('You are Logged Out');
        this.authService.signOut();
        this.authStatus = this.authService.isAuth;
    }

    onNewUser() {
        this.authService.signOut();
        this.authStatus = this.authService.isAuth;
        this.router.navigate(['newUser']);
    }
}
