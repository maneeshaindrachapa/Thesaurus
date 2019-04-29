import {Component, OnInit, ViewEncapsulation} from '@angular/core';
import {TranslateService} from '@ngx-translate/core';

@Component({
  selector: 'app-fullfirstpage',
  templateUrl: './fullfirstpage.component.html',
  styleUrls: ['./fullfirstpage.component.css'],
})
export class FullfirstpageComponent implements OnInit {

  public language = 'en';

  constructor(private translateService: TranslateService) {
    const savedLang = localStorage.getItem('lang');
    if (savedLang) {
      this.language = savedLang;
    }
  }

  ngOnInit() {
  }

  changeLang(lang) {
    this.language = lang;
    this.translateService.use(lang);
    this.translateService.setDefaultLang(lang);
    localStorage.setItem('lang', lang);
  }

}
