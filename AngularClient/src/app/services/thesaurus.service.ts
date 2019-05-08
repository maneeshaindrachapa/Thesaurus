import {EventEmitter, Injectable, Output} from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ThesaurusService {
  private host = 'http://127.0.0.1';
  private port = '5000';
  private base_url = this.host + ':' + this.port;
  @Output() public search_event = new EventEmitter();

  constructor(  private http: HttpClient
  ) { }

  public getThesaurusData(input_word, lang) {
    return this.http.post(this.base_url + '/thesaurus', {'word': input_word, 'lang': lang});
  }
}
