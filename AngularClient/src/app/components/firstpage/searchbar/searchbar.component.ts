import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {Router} from '@angular/router';
import {LanguagePredictService} from '../../../services/language-predict.service';
import {SpeechService} from 'ngx-speech';
import {SiTyperService} from '../../../services/si-typer.service';

@Component({
  selector: 'app-searchbar',
  templateUrl: './searchbar.component.html',
  styleUrls: ['./searchbar.component.css'],
  animations: [
  ],
})
export class SearchbarComponent implements OnInit {

  public input_word;
  public input_lang = 'en';
  public voice_search_enabled = false;

  // tslint:disable-next-line:max-line-length
  constructor(private router: Router, private langPredictService: LanguagePredictService, public speech: SpeechService, private siTyperService: SiTyperService) {
    siTyperService.wordSelected.subscribe((data) => {
      this.input_word = data;
      this.input_lang = 'si';
    });
  }

  ngOnInit() {
  }

  search() {
    if (this.input_word.trim()) {
      this.router.navigate(['/results'], {queryParams: {word: this.input_word, lang: this.input_lang}});
    }
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

  langIdentifier() {
    this.voice_search_inturrupt();
    this.langPredictService.predict(this.input_word).subscribe((data) => {
      if (data['response_code'] === 200) {
        this.input_lang = data['response_data']['language'];
      }
    });
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

  typer() {
      this.siTyperService.toggleTyper.emit();
  }

}
