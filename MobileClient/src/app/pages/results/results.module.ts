import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';

import { IonicModule } from '@ionic/angular';
import { ResultsPage } from './results.page';
import {TranslateModule} from '@ngx-translate/core';
import {SynonymsComponent} from './synonyms/synonyms.component';
import {DefinitionComponent} from './definition/definition.component';
import {ExamplesComponent} from './examples/examples.component';
import {RemoveUnderscorePipe} from '../../pipes/remove-underscore.pipe';

const routes: Routes = [
  {
    path: '',
    component: ResultsPage
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes),
    TranslateModule,
  ],
  declarations: [ResultsPage, SynonymsComponent, DefinitionComponent, ExamplesComponent, RemoveUnderscorePipe]
})
export class ResultsPageModule {}
