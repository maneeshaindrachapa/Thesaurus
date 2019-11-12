import { Component, OnInit } from '@angular/core';
import {ThesaurusService} from '../../services/thesaurus.service';
import {ActivatedRoute} from '@angular/router';
import {ServerConfig} from '../../services/serverConfig';

@Component({
  selector: 'app-results',
  templateUrl: './results.page.html',
  styleUrls: ['./results.page.scss'],
})

// @ts-ignore
export class ResultsPage implements OnInit {

  private segment = 'synonyms';
  private loading = true;
  // tslint:disable-next-line:variable-name
  private input_word;
  // tslint:disable-next-line:variable-name
  private input_lang;

  // tslint:disable-next-line:variable-name
  private response_data;

  private isAudioPlaying = false;

  constructor(private route: ActivatedRoute, private thesaurusService: ThesaurusService, private serverConfig: ServerConfig) {
    this.route.queryParams.subscribe(params => {
      this.input_word = params.word;
      this.input_lang = params.lang;
      this.getData();
    });
  }

  ngOnInit() {
  }

  getData() {
    this.loading = true;
    this.thesaurusService.getThesaurusData(this.input_word, this.input_lang).subscribe((data) => {
      this.response_data = data;
      if (this.response_data.response_code === 200) {
        this.response_data.response_data.synonyms.sort((a, b) => -1 * (parseFloat(a.similarity) - parseFloat(b.similarity)));
      }
      this.loading = false;
    });
  }

  // tslint:disable-next-line:variable-name
  playAudio(input_word) {
    this.isAudioPlaying = true;
    const audioObj = new Audio();
    audioObj.src = this.serverConfig.base_url + '/readword?word=' + input_word + '&lang=' + this.input_lang;
    audioObj.load();
    audioObj.play().then(() => {
      this.isAudioPlaying = false;
    });
  }

  contentChange(event: any) {
    this.segment = event.detail.value;
  }

}
