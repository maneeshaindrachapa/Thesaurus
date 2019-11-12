import { TestBed } from '@angular/core/testing';

import { SiTyperService } from './si-typer.service';

describe('SiTyperService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: SiTyperService = TestBed.get(SiTyperService);
    expect(service).toBeTruthy();
  });
});
