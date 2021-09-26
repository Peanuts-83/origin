import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators, FormArray, AbstractControl } from '@angular/forms';
import { Router } from '@angular/router';
import { CustomValidators } from '../custom-validators';
import { User } from '../models/user.model';
import { UserService } from '../services/user.service';

@Component({
    selector: 'app-new-user',
    templateUrl: './new-user.component.html',
    styleUrls: ['./new-user.component.scss']
})
export class NewUserComponent implements OnInit {
    userForm!: FormGroup;
    submitted = false;


    constructor(private formBuilder: FormBuilder,
                private userService:UserService,
                private router: Router) { }

    ngOnInit() {
        this.initForm();
    }

    initForm() {
        this.userForm = this.formBuilder.group({
            login: ['', [
                Validators.required,
                Validators.minLength(6)
            ]],
            password: ['', [
                Validators.required,
                Validators.minLength(8)
            ]],
            confirmPassword: '',
            firstname: '',
            lastname: '',
            email: ['', Validators.required],
            drinkPref: ['', Validators.required],
            hobbies: this.formBuilder.array([])
        },{
            validators: [
                CustomValidators.match('password','confirmPassword'),
                CustomValidators.emailCheck('email'),
                /* CustomValidators.hobbiesCheck('hobbies') */
            ]
        }
        );
    }

    get f(): {[key: string]: AbstractControl}  {
        return this.userForm.controls;
    }

    onSubmit() {
        this.submitted = true;
        if (this.userForm.invalid) {
            return;
        }

        const userId = this.userService.usersLength;
        const formVal = this.userForm.value
        const newUser = new User(
            userId,
            formVal.login,
            formVal.password,
            formVal.confirmPassword,
            formVal.firstname,
            formVal.lastname,
            formVal.email,
            formVal.drinkPref,
            formVal.hobbies ? formVal.hobbies : []
        );
        this.userService.addUser(newUser);
        this.submitted = false;
    }

    getHobbies() {
        return this.userForm.get('hobbies') as FormArray;
    }

    onAddHobby() {
        const newHobbyControl = this.formBuilder.control(null, Validators.required);
        this.getHobbies().push(newHobbyControl);
    }

}
