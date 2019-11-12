declare var $: any;

import {Component, EventEmitter, Input, OnInit} from '@angular/core';
import {SiTyperService} from '../../../services/si-typer.service';
import {NgbModal} from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-si-typer',
  templateUrl: './si-typer.component.html',
  styleUrls: ['./si-typer.component.css']
})
export class SiTyperComponent implements OnInit {


  private typedWord = '';
  private suggested;
  constructor(private siTyperService: SiTyperService) {
    this.siTyperService.toggleTyper.subscribe((data) => {
        this.typedWord = '';
        this.suggested = [];
        $('#siTyperModel').modal('show');
    });
  }

  ngOnInit() {
  }

  typiing() {
    this.siTyperService.getSuggetions(this.typedWord).subscribe((data) => {
      this.suggested = data[1][0][1];
      console.log(data[1][0][1]);
    });
  }

  selectWord(word) {
    this.siTyperService.wordSelected.emit(word);
    $('#siTyperModel').modal('hide');
  }

}
