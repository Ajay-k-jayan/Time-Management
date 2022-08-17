import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ManagertaskComponent } from './managertask/managertask.component';
import { TaskdetailsComponent } from './taskdetails/taskdetails.component';

const routes: Routes = [
  {
    path:'',
    redirectTo: 'dashboard',
    pathMatch: 'full'
  },
  {
    path:'dashboard',
    component:DashboardComponent
  },
  {
    path:'task',
    component:TaskdetailsComponent
  },
  {
    path: 'app-managertask',
    component:ManagertaskComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
