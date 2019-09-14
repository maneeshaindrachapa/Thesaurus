import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-loader-animation',
  templateUrl: './loader-animation.component.html',
  styleUrls: ['./loader-animation.component.css']
})
export class LoaderAnimationComponent implements OnInit {
  @Input() word: string;
  constructor() { }

  ngOnInit() {
  }

}
