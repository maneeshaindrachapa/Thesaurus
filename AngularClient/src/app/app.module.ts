import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SearchbarComponent } from './components/firstpage/searchbar/searchbar.component';
import { FullfirstpageComponent } from './components/firstpage/fullfirstpage/fullfirstpage.component';
import { FooterComponent } from './components/firstpage/footer/footer.component';
import { ResultsPageComponent } from './components/results-page/results-page.component';
import { NavBarComponent } from './components/results-page/nav-bar/nav-bar.component';
import { ResultsComponent } from './components/results-page/results/results.component';
import {FormsModule} from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    SearchbarComponent,
    FullfirstpageComponent,
    FooterComponent,
    ResultsPageComponent,
    NavBarComponent,
    ResultsComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }