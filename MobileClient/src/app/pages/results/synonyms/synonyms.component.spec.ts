import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SynonymsComponent } from './synonyms.component';

describe('SynonymsComponent', () => {
  let component: SynonymsComponent;
  let fixture: ComponentFixture<SynonymsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SynonymsComponent ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SynonymsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
