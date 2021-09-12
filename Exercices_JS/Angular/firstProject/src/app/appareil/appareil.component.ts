import { Component, OnInit, Input } from '@angular/core';
import { AppareilService } from '../services/appareil.service';


@Component({
  selector: 'app-appareil',
  templateUrl: './appareil.component.html',
  styleUrls: ['./appareil.component.scss']
})
export class AppareilComponent implements OnInit {

  @Input() appareilName!: string;
  @Input() appareilStatus!: string;
  @Input() id!: number;
  @Input() isAuth!: boolean;


  constructor(private appareilService: AppareilService) { }

  ngOnInit(): void { }

  isChecked() {
    if (this.appareilStatus === 'On') { return true }
    else { return false; }
  }

  onSwitch() {
    switch(this.appareilStatus) {
      case 'On':
        this.appareilService.switchOffOne(this.id-1);
        break;
      case 'Off':
        this.appareilService.switchOnOne(this.id-1);
        break;
    }
  }
}
