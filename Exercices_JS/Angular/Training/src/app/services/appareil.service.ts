import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { HttpClient } from '@angular/common/http'
import { Router } from '@angular/router';

@Injectable()
export class AppareilService {

    appareilSubject = new Subject<any[]>();
    private apps: any[] = [];
    /* [
        {
            id: 0,
            name: 'TV',
            status: 'On'
        },
        {
            id: 1,
            name: 'Ordi',
            status: 'On'
        },
        {
            id: 2,
            name: 'Washing Machine',
            status: 'Off'
        }
    ]; */

    constructor(private httpClient: HttpClient,
                private router: Router) { }

    saveAppareilsToServer() {
        // rename appareil.id to avoid duplicates
        this.apps.forEach((appareil,index) => {
            appareil.id = index;
        });
        this.httpClient
            .put('https://firstproject-aa4fd-default-rtdb.europe-west1.firebasedatabase.app/appareils.json', this.apps)
            .subscribe(
                () => {
                    console.log('Done!');
                    this.router.navigate(['/appareils']);
                },
                (error) => { console.log("Erreur d'enregistrement: " +error); });
    }

    getAppareilsFromServer() {
        this.httpClient
            .get<any[]>('https://firstproject-aa4fd-default-rtdb.europe-west1.firebasedatabase.app/appareils.json')
            .subscribe(
                (response) => {
                    this.apps = response;
                    this.emitAppareilSubject();
                },
                (error) => {
                    console.log('Erreur de récupération: ' +error);
                }
            )
    }

    addAppareil(name: string, status: string) {
        const appObject = {
            id: 0,
            name: '',
            status: ''
        };
        appObject.name = name;
        appObject.status = status;
        appObject.id = this.apps.length;
        this.apps.push(appObject);
        this.emitAppareilSubject();
    }


    emitAppareilSubject() {
        this.appareilSubject.next(this.apps);
    }

    getAppareilById(id: number) {
        const appareil = this.apps.find(
            ((x) => {
                return x.id === id;
            }));
        return appareil;
    }

    switchOnAll() {
        for (let appareil of this.apps) {
            appareil.status = 'On';
        }
        this.emitAppareilSubject();
        this.saveAppareilsToServer();
    }
    switchOffAll() {
        for (let appareil of this.apps) {
            appareil.status = 'Off';
        }
        this.emitAppareilSubject();
        this.saveAppareilsToServer();
    }

    switchOneOn(index: number) {
        this.apps[index].status = 'On';
        this.emitAppareilSubject();
        this.saveAppareilsToServer();
    }
    switchOneOff(index: number) {
        this.apps[index].status = 'Off';
        this.emitAppareilSubject();
        this.saveAppareilsToServer();
    }
    removeOne(index: number) {
        this.apps.splice(index, 1);
        this.emitAppareilSubject();
        this.saveAppareilsToServer();
    }

}
