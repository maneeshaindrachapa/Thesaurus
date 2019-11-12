import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SiTyperComponent } from './si-typer.component';

describe('SiTyperComponent', () => {
  let component: SiTyperComponent;
  let fixture: ComponentFixture<SiTyperComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SiTyperComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SiTyperComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
