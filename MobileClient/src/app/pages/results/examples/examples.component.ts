import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-examples',
  templateUrl: './examples.component.html',
  styleUrls: ['./examples.component.scss'],
})
export class ExamplesComponent implements OnInit {

  @Input()  private word;
  @Input()  private examplesData;

  constructor() { }

  ngOnInit() {}

  heighlightWord(word, sentence) {
    // tslint:disable-next-line:prefer-for-of
    for (let i = 0; i < word.split(word).length; i++) {
      sentence = sentence.toLowerCase().replace(word, '<b>' + word + '</b>');
    }
    return sentence;
  }

}
