import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SearchbarComponent } from './components/firstpage/searchbar/searchbar.component';
import { CardComponent } from './components/firstpage/card/card.component';
import { FullfirstpageComponent } from './components/firstpage/fullfirstpage/fullfirstpage.component';
import { FooterComponent } from './components/firstpage/footer/footer.component';

@NgModule({
  declarations: [
    AppComponent,
    SearchbarComponent,
    CardComponent,
    FullfirstpageComponent,
    FooterComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
