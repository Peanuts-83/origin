export class User {
    constructor (
        public userId: number,
        public login: string,
        public password: string,        //private?
        public confirmPassword: string,
        public firstname: string,
        public lastname: string,
        public email: string,
        public drinkPref: string,
        public hobbies?: string[]
    ) {}
}