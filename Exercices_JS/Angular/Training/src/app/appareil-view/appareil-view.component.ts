import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { AppareilService } from '../services/appareil.service';
import { AuthService } from '../services/auth.service';

@Component({
    selector: 'app-appareil-view',
    templateUrl: './appareil-view.component.html',
    styleUrls: ['./appareil-view.component.scss']
})
export class AppareilViewComponent implements OnInit, OnDestroy {

    isAuth = false;
    lastUpdate = new Promise<Date>((res, reject) => {
        const date = new Date();
        setTimeout(() => {
            res(date);
        }, 2000);
    })
    appareils!: any[];
    appareilSubscription!: Subscription;


    constructor(private appareilService: AppareilService,
        private authService: AuthService) { }


    ngOnInit() {
        this.appareilService.getAppareilsFromServer();
        this.appareilSubscription = this.appareilService.appareilSubject.subscribe(
            (apps: any[]) => this.appareils = apps
            // the same as :
            /* {
                next: (apps: any[]) => this.appareils = apps,
                error: (err) => console.log(err),
                complete: () => console.log('complete!')
            } */);

        this.appareilService.emitAppareilSubject();


        this.isAuth = this.authService.isAuth;
    }

    onAllumer() {
        this.appareilService.switchOnAll();
    }
    onEteindre() {
        this.appareilService.switchOffAll();
    }

    ngOnDestroy() {
        this.appareilSubscription.unsubscribe();
    }
}
