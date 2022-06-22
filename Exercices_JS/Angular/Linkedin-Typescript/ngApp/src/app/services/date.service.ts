import { getLocaleDateFormat } from '@angular/common';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DateService {
  date = new Date

  getDate() {
    return new Date()
  }

  constructor() { }
}
