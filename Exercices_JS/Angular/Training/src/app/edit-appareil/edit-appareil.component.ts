import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { AppareilService } from '../services/appareil.service';

@Component({
    selector: 'app-edit-appareil',
    templateUrl: './edit-appareil.component.html',
    styleUrls: ['./edit-appareil.component.scss']
})
export class EditAppareilComponent implements OnInit {

    constructor(private appareilService: AppareilService,
                private router: Router
                ) { }

    ngOnInit(): void {
    }

    onSubmit(f: NgForm) {
        console.log(f.value);
        const name = f.value['name'];
        const status = f.value['status'];
        this.appareilService.addAppareil(name, status);
        this.appareilService.saveAppareilsToServer()


        //this.router.navigate(['/appareils']);
    }
}
