import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { FullfirstpageComponent } from './components/firstpage/fullfirstpage/fullfirstpage.component';

const routes: Routes = [{path: '' , component: FullfirstpageComponent}];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
