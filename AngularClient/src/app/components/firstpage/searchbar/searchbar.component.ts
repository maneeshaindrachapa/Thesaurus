import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import {LanguagePredictService} from '../../../services/language-predict.service';

@Component({
  selector: 'app-searchbar',
  templateUrl: './searchbar.component.html',
  styleUrls: ['./searchbar.component.css']
})
export class SearchbarComponent implements OnInit {

  public input_word;
  public input_lang = 'en';
  public lang_detected = false;
  constructor(private router: Router, private langPredictService: LanguagePredictService) { }

  ngOnInit() {
  }

  search() {
    console.log('Search called!');
    this.router.navigate(['/results'], { queryParams: { word: this.input_word, lang: this.input_lang } });
  }

  langIdentifier() {
    this.langPredictService.predict(this.input_word).subscribe((data) => {
      this.input_lang = data['lang'];
    });
  }
}
