import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ResultPageUpdatedComponent } from './result-page-updated.component';

describe('ResultPageUpdatedComponent', () => {
  let component: ResultPageUpdatedComponent;
  let fixture: ComponentFixture<ResultPageUpdatedComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ResultPageUpdatedComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ResultPageUpdatedComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
