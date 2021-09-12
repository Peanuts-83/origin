export class AuthService {
    isAuth = false;

    signIn() {
        return new Promise((res, rej) => {
            setTimeout(() => {
                this.isAuth = true;
                res(true);
            }, 2000);
        })
    }

    signOut() {
        this.isAuth = false;
    }


}