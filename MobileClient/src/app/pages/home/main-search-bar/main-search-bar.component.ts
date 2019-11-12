import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import {LanguageIdentifierService} from '../../../services/language-identifier.service';
import {ThesaurusService} from '../../../services/thesaurus.service';

@Component({
  selector: 'app-main-search-bar',
  templateUrl: './main-search-bar.component.html',
  styleUrls: ['./main-search-bar.component.scss'],
})

// @ts-ignore
export class MainSearchBarComponent implements OnInit {

  // tslint:disable-next-line:variable-name
  private input_word;
  // tslint:disable-next-line:variable-name
  private input_lang = 'en';

  private suggetions;
  constructor(private languageItentifier: LanguageIdentifierService, private router: Router, private thesaurusService: ThesaurusService) { }

  ngOnInit() {}

  changeLang(lang) {
    this.input_lang = lang;
  }

  search() {
    if (this.input_word.trim()) {
      this.router.navigate(['/results'], {queryParams: {word: this.input_word, lang: this.input_lang}});
    }
  }

  suggetSearch(word){
    this.input_word = word;
    this.search();
  }

  langIdentifier() {
    this.getSuggetions();
    this.languageItentifier.predict(this.input_word).subscribe((data) => {
      if (data['response_code'] === 200) {
        this.input_lang = data['response_data']['language'];
      }
    });
  }

  getSuggetions() {
    this.thesaurusService.getSuggetions(this.input_word).subscribe((data: any) => {
      if(data.response_code == 200) {
        this.suggetions = data.response_data;
      }
    });
  }
}
