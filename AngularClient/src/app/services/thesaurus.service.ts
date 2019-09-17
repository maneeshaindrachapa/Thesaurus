import {EventEmitter, Injectable, Output} from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {ServerConfig} from './serverConfig';

@Injectable({
  providedIn: 'root'
})
export class ThesaurusService {

  @Output() public search_event = new EventEmitter();

  constructor(  private http: HttpClient, private serverConfig: ServerConfig
  ) { }

  public getThesaurusData(input_word, lang) {
    return this.http.post(this.serverConfig.base_url + '/thesaurus', {'word': input_word, 'language': lang});
  }
}
