import { Router } from '@angular/router';
import { AuthService } from './../../services/auth.service';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-signin',
    templateUrl: './signin.component.html',
    styleUrls: ['./signin.component.scss']
})
export class SigninComponent implements OnInit {

    signInForm!: FormGroup;
    errorMessage!: string;

    constructor(
        private formBuilder: FormBuilder,
        private authService: AuthService,
        private router: Router
    ) { }

    ngOnInit(): void {
        this.initForm();
    }

    initForm() {
        this.signInForm = this.formBuilder.group({
            email: ['', [Validators.required, Validators.email]],
            password: ['', [Validators.required, Validators.pattern(/[A-Z0-9]{6,}/i)]]
        });
    }

    onSubmit() {
        const email = this.signInForm.get('email')?.value;
        const password = this.signInForm.get('password')?.value;
        this.authService.signInUser(email, password)
            .then(
                () => { this.router.navigate(['/books']) },
                (error) => { this.errorMessage = error }
            )
    }
}
