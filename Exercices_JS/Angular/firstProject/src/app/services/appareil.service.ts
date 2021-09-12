import { Subject } from "rxjs";
import { HttpClient } from "@angular/common/http";
import { Injectable, OnInit } from "@angular/core";
import { Router } from '@angular/router';

@Injectable()
export class AppareilService {

    appareilSubject = new Subject<any[]>();

    private appareils: any[] = [];
    /* [
        {
            id: 1,
            name: 'Washing Machine',
            status: 'On'
        },
        {
            id: 2,
            name: 'Television',
            status: 'Off'
        },
        {
            id: 3,
            name: 'Fridge',
            status: 'On'
        },
    ] */

    constructor(private httpClient: HttpClient, private router: Router) {}

    ngOnInit() {}

    saveAppareilsToServer() {
        this.httpClient
            .put('https://firstproject-aa4fd-default-rtdb.europe-west1.firebasedatabase.app/appareils.json', this.appareils)
            .subscribe(() => {
                console.log('Enregistrement terminé!');
                this.router.navigate(['/appareils']);
            },
                (error) => {
                    console.log('Erreur: ' + error);
                });
    }

    getAppareilsFromServer() {
        this.httpClient
            .get<any[]>('https://firstproject-aa4fd-default-rtdb.europe-west1.firebasedatabase.app/appareils.json')
            .subscribe(
                (response) => {
                    this.appareils = response;
                    this.emitAppareilSubject();
                },
                (error) => {
                    console.log('Erreur: ' + error);
                });
    }

    getAppareilById(id: number) {
        return this.appareils.find(
            (appObject) => {
                return appObject.id === id;
            }
        );
    }

    emitAppareilSubject() {
        this.appareilSubject.next(this.appareils.slice());
    }

    onSwitchOnAll() {
        for (let app of this.appareils) {
            app.status = 'On';
        }
    }

    onSwitchOffAll() {
        for (let app of this.appareils) {
            app.status = 'Off';
        }
    }

    switchOnOne(i: number) {
        this.appareils[i].status = 'On';
    }

    switchOffOne(i: number) {
        this.appareils[i].status = 'Off';
    }

    addAppareil(name: string, status: string) {
        const newObj = {
            id: 0,
            name: '',
            status: ''
        };
        newObj.name = name;
        newObj.status = status;
        newObj.id = this.appareils.length + 1;
        this.appareils.push(newObj);
        this.emitAppareilSubject();
    }

}