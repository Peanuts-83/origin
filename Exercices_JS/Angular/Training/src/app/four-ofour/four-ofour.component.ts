import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-four-ofour',
  templateUrl: './four-ofour.component.html',
  styleUrls: ['./four-ofour.component.scss']
})
export class FourOfourComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit(): void {
      setTimeout(() => {
        this.router.navigate(['/appareils']);
      }, 2000);
  }

}
