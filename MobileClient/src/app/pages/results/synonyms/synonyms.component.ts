import { Component, OnInit } from '@angular/core';
import {Platform} from '@ionic/angular';

@Component({
  selector: 'app-synonyms',
  templateUrl: './synonyms.component.html',
  styleUrls: ['./synonyms.component.scss'],
})
export class SynonymsComponent implements OnInit {

  private height;
  constructor(private platform: Platform) {
    this.height = platform.height();
  }

  ngOnInit() {}

}
