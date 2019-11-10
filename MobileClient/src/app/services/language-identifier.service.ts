import { Injectable } from '@angular/core';
import {ServerConfig} from './serverConfig';
import {HttpClient, HttpHeaders} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class LanguageIdentifierService {

  constructor(private http: HttpClient, private serverConfig: ServerConfig) {

  }

  getHeaders(): HttpHeaders {
    const headers = new HttpHeaders();
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append ('Content-Type', 'application/json; charset=utf-8');
    headers.append('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    headers.append('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE, OPTIONS');
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'application/json');
    return headers;
  }

  predict(word) {
    console.log(this.serverConfig.base_url);
    return this.http.post('http://thesaurus.projects.uom.lk:5000/language', { word : word},   { headers: this.getHeaders() });
  }

  test() {
    return this.http.get('http://thesaurus.projects.uom.lk:5000', { headers: this.getHeaders() });
  }
}
