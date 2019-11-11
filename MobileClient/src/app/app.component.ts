import { Component } from '@angular/core';

import { Platform } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';
import {TranslateService} from '@ngx-translate/core';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss']
})
export class AppComponent {
  // tslint:disable-next-line:variable-name
  private appLang = 'en'

  constructor(
    private platform: Platform,
    private splashScreen: SplashScreen,
    private statusBar: StatusBar,
    private translate: TranslateService
  ) {
    this.initializeApp();
  }

  initializeApp() {
    this.platform.ready().then(() => {
      this.statusBar.styleDefault();
      this.splashScreen.hide();
    });

    const savedLang = localStorage.getItem('lang');
    if (savedLang) {
      this.appLang = savedLang;
      this.translate.setDefaultLang(savedLang);
      this.translate.use(savedLang);
    } else {
      this.translate.setDefaultLang('en');
      this.translate.use('en');
    }
  }

  changeLang() {
    localStorage.setItem('lang', this.appLang);
    this.translate.setDefaultLang(this.appLang);
    this.translate.use(this.appLang);
  }
}
