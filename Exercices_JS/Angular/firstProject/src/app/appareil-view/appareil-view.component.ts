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

	lastDate = new Promise<Date>((resolve, reject) => {
		const date = new Date();
		setTimeout(() => {
			resolve(date);
		}, 2000);
	});

	authStatus!: boolean;
	appareils!: any[];
	appareilSubscription!: Subscription;


	constructor(private appareilService: AppareilService, private authService: AuthService) { };

	ngOnInit() {
		this.appareilService.getAppareilsFromServer();
		this.appareilSubscription = this.appareilService
									.appareilSubject
									.subscribe(
										(appareils: any[]) => {
											this.appareils = appareils;});
		this.appareilService.emitAppareilSubject();
		this.authStatus = this.authService.isAuth;
	};

	authValue() { return this.authStatus };

	switchOn() {
		this.appareilService.onSwitchOnAll();
	};

	switchOff() {
		if (confirm('Are you sure to switch off all your stuff?')) {
			this.appareilService.onSwitchOffAll();
		}
		return null;
	};

	ngOnDestroy() {
		this.appareilSubscription.unsubscribe();
	}
/*
	onSave() {
		this.appareilService.saveAppareilsToServer();
	} */
}
