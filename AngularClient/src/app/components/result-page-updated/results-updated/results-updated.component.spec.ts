import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ResultsUpdatedComponent } from './results-updated.component';

describe('ResultsUpdatedComponent', () => {
  let component: ResultsUpdatedComponent;
  let fixture: ComponentFixture<ResultsUpdatedComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ResultsUpdatedComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ResultsUpdatedComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
