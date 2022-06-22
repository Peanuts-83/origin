import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-train',
  templateUrl: './train.component.html',
  styleUrls: ['./train.component.css']
})
export class TrainComponent implements OnInit {
  trainData!: any

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.http
      .get('http://transport.opendata.ch/v1/connections?from=Lausanne&to=Genève')
      .subscribe(value => {
          this.trainData = value
      })

  }

}
