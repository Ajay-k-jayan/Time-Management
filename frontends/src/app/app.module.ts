import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { SidenavComponent } from './sidenav/sidenav.component';
import { AddtaskComponent } from './addtask/addtask.component';
import { TaskdetailsComponent } from './taskdetails/taskdetails.component';
import { DashboardComponent } from './dashboard/dashboard.component';

import { ManagertaskComponent } from './managertask/managertask.component';
import { AppManagerSideNavComponent } from './app-manager-side-nav/app-manager-side-nav.component';

import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
;

// pipe
import { SearchPipe } from './search.pipe';
// chart
import { ChartModule } from 'angular2-chartjs';




@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    SidenavComponent,
    AddtaskComponent,
    TaskdetailsComponent,
    DashboardComponent,
    SearchPipe,
    ManagertaskComponent,
    AppManagerSideNavComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    ChartModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
