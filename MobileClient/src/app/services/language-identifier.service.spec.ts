import { TestBed } from '@angular/core/testing';

import { LanguageIdentifierService } from './language-identifier.service';

describe('LanguageIdentifierService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: LanguageIdentifierService = TestBed.get(LanguageIdentifierService);
    expect(service).toBeTruthy();
  });
});
