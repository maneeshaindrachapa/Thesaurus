import {Component, Input, OnInit} from '@angular/core';
import {AlertController, Platform} from '@ionic/angular';
import {ServerConfig} from '../../../services/serverConfig';
import {ThesaurusService} from '../../../services/thesaurus.service';
import {Router} from '@angular/router';
import {TranslateService} from '@ngx-translate/core';

@Component({
  selector: 'app-synonyms',
  templateUrl: './synonyms.component.html',
  styleUrls: ['./synonyms.component.scss'],
})

// @ts-ignore
export class SynonymsComponent implements OnInit {

  private height;
  // @ts-ignore
  @Input() private synonyms;
  // @ts-ignore
  @Input() private lang;

  constructor(private platform: Platform,   private serverConfig: ServerConfig, private thesaurusService: ThesaurusService, private router: Router, private alertController: AlertController, private translateService: TranslateService) {
    this.height = platform.height();
  }

  ngOnInit() {}

  search(input_word) {
    if (input_word.trim()) {
      this.router.navigate(['/results'], {queryParams: {word: input_word, lang: this.lang}});
    }
  }

  playAudio(input_word, elem) {
    document.getElementById(elem).classList.add('audio-playing');
    const audioObj = new Audio();
    audioObj.src = this.serverConfig.base_url + '/readword?word=' + input_word + '&lang=' + this.lang;
    audioObj.load();
    audioObj.play().then(() => {
      document.getElementById(elem).classList.remove('audio-playing');
    });
  }

  translate(word){
    this.thesaurusService.getTranslation(word,this.lang).subscribe((data: any) => {
      this.translateService.get("TRANSLATED_WORD").subscribe((res) => {
        this.showTranslated(res ,data.response_data[0]);
      });
    });
  }

  async showTranslated(header ,word) {
    const alert = await this.alertController.create({
      header: header,
      message: word,
      backdropDismiss:false,
      buttons: [
        {
          text: 'Cose',
          role: 'close'
          }
      ]
    });
    await alert.present();
  }


}
