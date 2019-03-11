import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'jz-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'mebears app';

  constructor(private http: HttpClient) {}


  ngOnInit(): void {
    this.http.get('http://localhost:8000/getData').subscribe(data => {
      console.log(data);
    });
  }

}
