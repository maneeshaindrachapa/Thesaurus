import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-definition',
  templateUrl: './definition.component.html',
  styleUrls: ['./definition.component.scss'],
})
export class DefinitionComponent implements OnInit {

  @Input()  private word;
  @Input()  private definitionData;

  constructor() { }

  ngOnInit() {}

}
