import { Component, Input, OnInit } from '@angular/core';
import { AppareilService } from '../services/appareil.service';
import { AuthService } from '../services/auth.service';


@Component({
  selector: 'app-appareil',
  templateUrl: './appareil.component.html',
  styleUrls: ['./appareil.component.scss']
})
export class AppareilComponent implements OnInit {

  @Input() appareilName!: string;
  @Input() appareilStatus!: string;
  @Input() appareilId!: number;

  constructor(private appareilService: AppareilService,
                private authService: AuthService) { }

  ngOnInit(): void {}

  isAuth = this.authService.isAuth;

  getColor() {
    if (this.appareilStatus === 'On') {
      return 'green';
    } else {
      return 'red';
    }
  }

  onSwitchOn() {
    this.appareilService.switchOneOn(this.appareilId);
  }
  onSwitchOff() {
    this.appareilService.switchOneOff(this.appareilId);
  }
  onRemove() {
      this.appareilService.removeOne(this.appareilId);
  }
}
