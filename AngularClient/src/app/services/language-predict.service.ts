import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {ServerConfig} from './serverConfig';

@Injectable({
  providedIn: 'root'
})
export class LanguagePredictService {

  constructor(private http: HttpClient, private serverConfig: ServerConfig) { }

  predict(word) {
    return this.http.post(this.serverConfig.base_url + '/language', {'word': word});
  }

  spellCheck(word, lang) {
    return this.http.get(this.serverConfig.base_url + '/spellcheck?word=' + word + '&lang=' + lang);
  }
}
