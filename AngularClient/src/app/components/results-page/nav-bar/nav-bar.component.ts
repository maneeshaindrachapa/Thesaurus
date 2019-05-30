import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {ThesaurusService} from '../../../services/thesaurus.service';
import {LanguagePredictService} from '../../../services/language-predict.service';
import {SpeechService} from 'ngx-speech';

@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.css'],

})
export class NavBarComponent implements OnInit {

  public input_word;
  public input_lang = 'en';
  public voice_search_enabled = false;

  constructor(private router: Router, private route: ActivatedRoute, private thesaurusService: ThesaurusService, private langPredictService: LanguagePredictService, public speech: SpeechService) {

    thesaurusService.search_event.subscribe((data) => {
      this.router.navigate(['/results'], { queryParams: { word: data[0], lang: data[1] } });
      this.input_word = data[0];
    });
  }

  ngOnInit() {
    this.route.queryParams.subscribe(params => {
      this.input_word = params.word;
    });
  }

  search() {
    console.log('Search called!');
    this.router.navigate(['/results'], { queryParams: { word: this.input_word, lang: this.input_lang } });
    this.thesaurusService.search_event.emit([this.input_word, this.input_lang]);

  }

  langIdentifier() {
    this.langPredictService.predict(this.input_word).subscribe((data) => {
      this.input_lang = data['lang'];
    });
  }

  voiceType() {
    if (this.voice_search_enabled) {
      this.speech.stop();
    } else {
      this.speech.recognition.lang = this.input_lang === 'si' ? 'si-LK' : 'en-US';
      this.speech.start();
      this.speech.message.subscribe((data) => {
        this.input_word = data.message;
        this.voice_search_inturrupt();
        this.search();
      });
    }
    this.voice_search_enabled = !this.voice_search_enabled;
  }

  onLangChange(lang) {
    this.voice_search_inturrupt();
  }

  voice_search_inturrupt() {
    if (this.voice_search_enabled) {
      this.voice_search_enabled = false;
      this.speech.stop();
    }
  }

}
