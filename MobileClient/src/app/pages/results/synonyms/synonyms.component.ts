import {Component, Input, OnInit} from '@angular/core';
import {Platform} from '@ionic/angular';
import {ServerConfig} from '../../../services/serverConfig';
import {ThesaurusService} from '../../../services/thesaurus.service';

@Component({
  selector: 'app-synonyms',
  templateUrl: './synonyms.component.html',
  styleUrls: ['./synonyms.component.scss'],
})

// @ts-ignore
export class SynonymsComponent implements OnInit {

  private height;
  // @ts-ignore
  @Input() private synonyms;
  // @ts-ignore
  @Input() private lang;

  constructor(private platform: Platform,   private serverConfig: ServerConfig, private thesaurusService: ThesaurusService) {
    this.height = platform.height();
  }

  ngOnInit() {}

  playAudio(input_word, elem) {
    document.getElementById(elem).classList.add('audio-playing');
    const audioObj = new Audio();
    audioObj.src = this.serverConfig.base_url + '/readword?word=' + input_word + '&lang=' + this.lang;
    audioObj.load();
    audioObj.play().then(() => {
      document.getElementById(elem).classList.remove('audio-playing');
    });
  }

}
