import { AbstractControl, ValidatorFn } from "@angular/forms";

export class CustomValidators {


    static match(password: string, confirmPassword: string)
        :
        ValidatorFn {
        return (controls: AbstractControl) => {
            const control = controls.get(password);
            const checkControl = controls.get(confirmPassword);
            if (checkControl!.errors && !checkControl!.errors.matching) {
                return null;
            }
            if (control!.value !== checkControl!.value) {
                controls.get(confirmPassword)?.setErrors({ matching: true });
                return { matching: true };
            } else {
                return null;
            }
        }
    }

    static emailCheck(mail: string)
        :
        ValidatorFn {
        return (controls: AbstractControl) => {
            const email = controls.get(mail);
            const regexp = new RegExp(/([A-Z0-9]*@[A-Z0-9]*)\w+.[A-Z]{2,}$/gi);
            if (regexp.test(email!.value)) {
                return null;
            } else {
                controls.get(mail)?.setErrors({ matching: true });
                return { matching: true };
            };
        }
    }

    static hobbiesCheck(hobbies: string | (string | number)[])
    :
    ValidatorFn {
        return (controls: AbstractControl) => {
            const hobbyList = controls.get(hobbies)!.value;
            hobbyList!.array.forEach((hobby: any) => {
                console.log(hobby);
            });
            return null;
        }
    }

    /* static idCheck(login: string, password: string)
    :
    ValidatorFn {
        return (controls: AbstractControl) => {

        }
    } */

}
