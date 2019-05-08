import { TestBed } from '@angular/core/testing';

import { PosTagService } from './pos-tag.service';

describe('PosTagService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: PosTagService = TestBed.get(PosTagService);
    expect(service).toBeTruthy();
  });
});
