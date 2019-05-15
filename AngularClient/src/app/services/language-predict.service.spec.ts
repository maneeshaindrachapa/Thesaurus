import { TestBed } from '@angular/core/testing';

import { LanguagePredictService } from './language-predict.service';

describe('LanguagePredictService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: LanguagePredictService = TestBed.get(LanguagePredictService);
    expect(service).toBeTruthy();
  });
});
