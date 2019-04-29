import { Component } from '@angular/core';
import {TranslateService} from '@ngx-translate/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Thesaurus';
  constructor(private translate: TranslateService) {
    const savedLang = localStorage.getItem('lang');
    if (savedLang) {
      translate.setDefaultLang(savedLang);
      translate.use(savedLang);
    } else {
      translate.setDefaultLang('en');
      translate.use('en');
    }
  }
}
