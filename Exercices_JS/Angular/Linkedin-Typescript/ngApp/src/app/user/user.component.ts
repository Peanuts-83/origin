import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { DateService } from '../services/date.service';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {
  userForm = new FormGroup({
    name: new FormControl('Bill'),
    email: new FormControl('a@b.com')
  })

  showForm() {
    console.log(this.userForm.value)
  }


  constructor(public dateService: DateService) {
   }

  ngOnInit(): void {
    this.dateService.date
  }

}
