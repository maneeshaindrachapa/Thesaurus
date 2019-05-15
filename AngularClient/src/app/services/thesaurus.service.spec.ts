import { TestBed } from '@angular/core/testing';
import { ThesaurusService } from './thesaurus.service';

describe('ThesaurusService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ThesaurusService = TestBed.get(ThesaurusService);
    expect(service).toBeTruthy();
  });
});
