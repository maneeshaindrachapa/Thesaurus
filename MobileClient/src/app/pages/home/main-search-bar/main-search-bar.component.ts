import { Component, OnInit } from '@angular/core';
import {LanguageIdentifierService} from '../../../services/language-identifier.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-main-search-bar',
  templateUrl: './main-search-bar.component.html',
  styleUrls: ['./main-search-bar.component.scss'],
})
export class MainSearchBarComponent implements OnInit {

  // tslint:disable-next-line:variable-name
  private input_word;
  // tslint:disable-next-line:variable-name
  private input_lang = 'en';

  constructor(private languageItentifier: LanguageIdentifierService, private router: Router) { }

  ngOnInit() {}

  changeLang(lang) {
    this.input_lang = lang;
  }

  search() {
    this.router.navigate(['/results']);
  }

  langIdentifier() {
    this.languageItentifier.predict(this.input_word).subscribe((data) => {
      if (data['response_code'] === 200) {
        this.input_lang = data['response_data']['language'];
      }
    });
  }

  test(){
    this.languageItentifier.test().subscribe((data)=>{
      console.log(data);
    });
  }

}
