import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-fullfirstpage',
  templateUrl: './fullfirstpage.component.html',
  styleUrls: ['./fullfirstpage.component.css']
})
export class FullfirstpageComponent implements OnInit {

  public language = 'EN';

  constructor() {
    const savedLang = localStorage.getItem('lang');
    if (savedLang) {
      this.language = savedLang;
    }
  }

  ngOnInit() {
  }

  changeLang(lang) {
    this.language = lang;
    localStorage.setItem('lang', lang);
  }

}
