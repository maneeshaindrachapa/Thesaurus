import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { FullfirstpageComponent } from './components/firstpage/fullfirstpage/fullfirstpage.component';
import { ResultsPageComponent } from './components/results-page/results-page.component';

const routes: Routes = [{ path: '', component: FullfirstpageComponent },
{ path: 'results', component: ResultsPageComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
