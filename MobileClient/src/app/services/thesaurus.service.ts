import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {ServerConfig} from './serverConfig';

@Injectable({
  providedIn: 'root'
})
export class ThesaurusService {

  constructor(  private http: HttpClient, private serverConfig: ServerConfig) { }

  // tslint:disable-next-line:variable-name
  public getThesaurusData(input_word, lang) {
    return this.http.post(this.serverConfig.base_url + '/thesaurus', {'word': this.whiteSpaceToUnderscore(input_word), 'language': lang});
  }

  public whiteSpaceToUnderscore(word) {
    // tslint:disable-next-line:prefer-for-of
    for (let i = 0; i < word.split(' ').length; i++) {
      word = word.replace(' ', '_');
    }
    return word;
  }

  public underscoreToWhiteSpace(word) {
    // tslint:disable-next-line:prefer-for-of
    for (let i = 0; i < word.split('_').length; i++) {
      word = word.replace('_', ' ');
    }
    return word;
  }
}
