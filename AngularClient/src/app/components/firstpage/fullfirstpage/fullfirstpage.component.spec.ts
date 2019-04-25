import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FullfirstpageComponent } from './fullfirstpage.component';

describe('FullfirstpageComponent', () => {
  let component: FullfirstpageComponent;
  let fixture: ComponentFixture<FullfirstpageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FullfirstpageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FullfirstpageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
