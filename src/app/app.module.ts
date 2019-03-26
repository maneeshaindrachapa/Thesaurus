import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SearchbarComponent } from './components/firstpage/searchbar/searchbar.component';
import { CardComponent } from './components/firstpage/card/card.component';
import { FullfirstpageComponent } from './components/firstpage/fullfirstpage/fullfirstpage.component';

@NgModule({
  declarations: [
    AppComponent,
    SearchbarComponent,
    CardComponent,
    FullfirstpageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
