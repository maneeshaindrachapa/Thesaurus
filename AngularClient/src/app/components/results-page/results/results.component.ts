import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {ThesaurusService} from '../../../services/thesaurus.service';
import {PosTagService} from '../../../services/pos-tag.service';

@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.css']
})
export class ResultsComponent implements OnInit {
  public input_word;
  public input_lang;
  public response_data;


  constructor(private route: ActivatedRoute, private thesaurusService: ThesaurusService, private posTagService: PosTagService) {
    this.route.queryParams.subscribe(params => {
      this.input_word = params.word;
      this.input_lang = params.lang;
    });
    this.getData();
    thesaurusService.search_event.subscribe((data) => {
      this.input_word = data[0];
      this.input_lang = data[1];
      this.getData();
    });
  }

  ngOnInit() {
  }

  getData() {
    this.thesaurusService.getThesaurusData(this.input_word, this.input_lang).subscribe((data) => {
      this.response_data = data;
      console.log(data);
    });
  }

  search(input_word, lang) {
    this.thesaurusService.search_event.emit([input_word,lang]);
  }
}
