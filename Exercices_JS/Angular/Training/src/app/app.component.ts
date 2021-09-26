import { Component, OnDestroy, OnInit } from '@angular/core';
import { Observable, Subscription } from 'rxjs';
import 'rxjs/add/observable/interval';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit, OnDestroy {

    secondes!: number;
    subscription!: Subscription;

    ngOnInit() {
        const counter = Observable.interval(1000);
        this.subscription = counter.subscribe(
            (val) => {
                this.secondes = val;
                if (this.secondes >= 3) { this.ngOnDestroy();}
            },
            (error) => {
                console.log(error);
            },
            () => {
                console.log('Observable complete!');
            }
        )
    }

    ngOnDestroy() {
        this.subscription.unsubscribe();
    }

}
