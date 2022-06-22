import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  user: string = 'Tom'
  elements = [1, 2, 3]
  images = [
    'assets/f957375061e528fbbb2e3c84bbd0fdb6.jpg',
    'assets/il_fullxfull.223662570.webp',
    'assets/peanuts-charlie-brown-snoopy-70x100cm-affic.webp'
  ]

  userClick() {
    console.log('Clicked!')
  }


  constructor() { }

  ngOnInit(): void {
  }

}
