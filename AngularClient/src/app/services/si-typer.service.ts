import {EventEmitter, Injectable, Output} from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class SiTyperService {

  @Output() public toggleTyper = new EventEmitter();

  @Output() public wordSelected = new EventEmitter();

  constructor(private http: HttpClient) { }

  public getSuggetions(word) {
    // tslint:disable-next-line:max-line-length
    return this.http.get('https://www.google.com/inputtools/request?text=' + word + '&ime=transliteration_en_si&num=5&cp=0&cs=0&ie=utf-8&oe=utf-8&app=jsapi');
  }
}
