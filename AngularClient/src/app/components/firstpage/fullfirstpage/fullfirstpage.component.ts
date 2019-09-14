import {Component, OnInit, ViewEncapsulation} from '@angular/core';
import {TranslateService} from '@ngx-translate/core';

@Component({
  selector: 'app-fullfirstpage',
  templateUrl: './fullfirstpage.component.html',
  styleUrls: ['./fullfirstpage.component.css'],
})
export class FullfirstpageComponent implements OnInit {


  constructor(private translateService: TranslateService) {

  }

  ngOnInit() {
  }
}
