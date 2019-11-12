import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SearchbarComponent } from './components/firstpage/searchbar/searchbar.component';
import { FullfirstpageComponent } from './components/firstpage/fullfirstpage/fullfirstpage.component';
import { FooterComponent } from './components/utilities/footer/footer.component';
import { ResultsPageComponent } from './components/results-page/results-page.component';
import { NavBarComponent } from './components/results-page/nav-bar/nav-bar.component';
import { ResultsComponent } from './components/results-page/results/results.component';
import {FormsModule} from '@angular/forms';
import {TranslateLoader, TranslateModule, TranslateService} from '@ngx-translate/core';
import {HttpClient, HttpClientModule} from '@angular/common/http';
import {TranslateHttpLoader} from '@ngx-translate/http-loader';
import {ThesaurusService} from './services/thesaurus.service';
import { LoadingBarHttpClientModule } from '@ngx-loading-bar/http-client';
import { LoadingBarModule } from '@ngx-loading-bar/core';
import {LanguagePredictService} from './services/language-predict.service';
import {ServerConfig} from './services/serverConfig';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {SpeechModule} from 'ngx-speech';
import { LoaderAnimationComponent } from './components/results-page/loader-animation/loader-animation.component';
import { LanguageSwitchComponent } from './components/utilities/language-switch/language-switch.component';
import { ResultsV2Component } from './components/results-page/results-v2/results-v2.component';
import { RemoveUnderscorePipe } from './pipes/remove-underscore.pipe';
import {SiTyperService} from './services/si-typer.service';
import {SiTyperComponent} from './components/firstpage/si-typer/si-typer.component';


@NgModule({
  declarations: [
    AppComponent,
    SearchbarComponent,
    FullfirstpageComponent,
    FooterComponent,
    ResultsPageComponent,
    NavBarComponent,
    ResultsComponent,
    LoaderAnimationComponent,
    LanguageSwitchComponent,
    ResultsV2Component,
    RemoveUnderscorePipe,
    SiTyperComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    FormsModule,
    HttpClientModule,
    TranslateModule.forRoot({
      loader: {
        provide: TranslateLoader,
        useFactory: (createTranslateLoader),
        deps: [HttpClient]
      }
    }),
    LoadingBarHttpClientModule,
    SpeechModule

  ],
  providers: [ThesaurusService, LanguagePredictService, ServerConfig, { provide: 'SPEECH_LANG', useValue: 'en-US' }, SiTyperService],
  bootstrap: [AppComponent]
})
export class AppModule { }

export function createTranslateLoader(http: HttpClient) {
  return new TranslateHttpLoader(http, './assets/i18n/', '.json');
}
