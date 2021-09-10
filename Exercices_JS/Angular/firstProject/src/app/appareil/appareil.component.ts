import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-appareil',
  templateUrl: './appareil.component.html',
  styleUrls: ['./appareil.component.scss']
})
export class AppareilComponent implements OnInit {
  //appareilName : string = 'Machine à laver';
  @Input() appareilName: string = '';
  //appareilStatus: string = 'éteint';
  @Input() appareilStatus: string = '';

  constructor() { }

  ngOnInit() { }

  getStatus() {
    return this.appareilStatus;
  }

  getColor() {
    if (this.appareilStatus === 'allumé') {return 'green'}
    else if (this.appareilStatus === 'éteint') {return 'red'}
    else {return 'lightgrey'}
  }

}
