import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'removeUnderscore'
})
export class RemoveUnderscorePipe implements PipeTransform {

  transform(value: string, args?: any): any {
    for (let i = 0; i < value.split('_').length; i++) {
      value = value.replace('_', ' ');
    }
    return value;
  }

}
