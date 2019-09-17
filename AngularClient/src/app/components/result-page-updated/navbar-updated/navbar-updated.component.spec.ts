import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NavbarUpdatedComponent } from './navbar-updated.component';

describe('NavbarUpdatedComponent', () => {
  let component: NavbarUpdatedComponent;
  let fixture: ComponentFixture<NavbarUpdatedComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NavbarUpdatedComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NavbarUpdatedComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
