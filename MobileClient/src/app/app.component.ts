import { Component } from '@angular/core';

import {AlertController, Platform} from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';
import {TranslateService} from '@ngx-translate/core';
import {OpenNativeSettings} from '@ionic-native/open-native-settings/ngx';
import { Network } from '@ionic-native/network/ngx';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss']
})
export class AppComponent {
  // tslint:disable-next-line:variable-name
  private appLang = 'en'
  private net_alert;
  constructor(
    private platform: Platform,
    private splashScreen: SplashScreen,
    private statusBar: StatusBar,
    private translate: TranslateService,
    public alertController: AlertController,
    private openNativeSettings: OpenNativeSettings,
    private network: Network
  ) {
    this.initializeApp();
  }

  initializeApp() {
    this.platform.ready().then(() => {
      this.statusBar.styleDefault();
      this.splashScreen.hide();
      this.connEventSubscription();
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


  connEventSubscription(){
    this.network.onConnect().subscribe(() => {
      console.log('network connected!');
      console.log(this.net_alert);
      if(this.net_alert) {
        this.net_alert.dismiss();
      }
    });
    this.network.onDisconnect().subscribe(() => {
        if(!this.net_alert) {
            this.networkAlert();
        }
    });
  }

  async networkAlert() {
    const alert = await this.alertController.create({
      header: 'No Internet Connection',
      message: '<div class="w-100 text-center"><i class="fas fa-exclamation-triangle fa-4x" ></i><br><br>Sorry! Not detected any Internet connection. Please reconnect and try again.</div>',
      backdropDismiss:false,
      buttons: [
        {
          text: 'Open Settings',
            handler: (blah) => {
              this.openNativeSettings.open("settings").then(()=>{
              });
            }
        }, {
          text: 'Exit',
              handler: () => {
                navigator['app'].exitApp();
           }
        }
      ]
    });
    this.net_alert = await alert;
    await alert.present();
  }

}
