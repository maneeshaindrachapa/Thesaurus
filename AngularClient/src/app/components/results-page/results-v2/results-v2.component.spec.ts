import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ResultsV2Component } from './results-v2.component';

describe('ResultsV2Component', () => {
  let component: ResultsV2Component;
  let fixture: ComponentFixture<ResultsV2Component>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ResultsV2Component ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ResultsV2Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
