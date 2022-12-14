import { NgStyle } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { TaskapiService } from '../services/taskapi.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  TaskLists: any = [];
  public totalCompleted = 0;
  public totalProgress = 0;
  constructor(private service: TaskapiService) { }

  // approval statys
  public totalApproval = 0;

  // graph
  public type: any;
  public data: any;
  public options: any;

  // doughnut
  public types: any;
  public datas: any;
  public options2: any;

  // months
  public januaryTotal = 0;
  public febTotal = 0;
  public marTotal = 0;
  public aprilTotal = 0;
  public mayTotal = 0;
  public juneTotal = 0;
  public julyTotal = 0;
  public augTotal = 0;
  public sepTotal = 0;
  public octTotal = 0;
  public novTotal = 0;
  public decTotal = 0;



  ngOnInit(): void {
    this.refreshTaskList();

  }
  refreshTaskList() {
    this.service.getAll().subscribe(data => {
      this.TaskLists = data;
      // getting cards data task
        for (let entry of this.TaskLists) {
          // no of completed task
          if (entry.Status == "Completed") {
            this.totalCompleted += 1;

          }
          // no of progress task
          else {
            this.totalProgress += 1;

          }
          // no of approval task
          if (entry.ApprovalStatus == "Approved"){
            this.totalApproval +=1;
          }
        }
        // console.log("completed = ", this.totalCompleted);
        // console.log("In Progress = ", this.totalProgress);


        // doughnut
        this.types = 'doughnut';
        this.datas = {
          labels: ["Completed", "In Progress"],
          datasets: [
            {
              data: [this.totalCompleted, this.totalProgress],
              backgroundColor: ['#1B2430', '#B2B1B9']
            }
          ]
        };

        this.options2 = {
          legend: {
            display: true
          },
          responsive: true,
          maintainAspectRatio: false
        }

        for (let entrys of this.TaskLists) {
          var date = new Date(entrys.CreatedDate);
          var month = date.getMonth();
          // console.log("month", month);
          // jan
          if (month == 0) {
            this.januaryTotal += 1;
          }
          // feb
          else if (month == 1) {
            this.febTotal += 1;
          }
          // march
          else if (month == 2) {
            this.marTotal += 1;
          }
          // april
          else if (month == 3) {
            this.aprilTotal += 1;
          }
          // may
          else if (month == 4) {
            this.mayTotal += 1;
          }
          // june
          else if (month == 5) {
            this.juneTotal += 1;
          }
          // july
          else if (month == 6) {
            this.julyTotal += 1;
          }
          // august
          else if (month == 7) {
            this.augTotal += 1;
          }
          // sept
          else if (month == 8) {
            this.sepTotal += 1;
          }
          // oct
          else if (month == 9) {
            this.octTotal += 1;
          }
          // nov
          else if (month == 10) {
            this.novTotal += 1;
          }
          // dec
          else {
            this.decTotal += 1;
          }
        }
        // graph
        this.type = 'bar';
        this.data = {
          labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
          datasets: [
            {
              label: "Number of Projects in months",
              fill: 'true',
              backgroundColor: "#263333",
              data: [this.januaryTotal, this.febTotal, this.marTotal, this.aprilTotal, this.mayTotal, this.juneTotal, this.julyTotal, this.augTotal, this.sepTotal, this.octTotal, this.novTotal, this.decTotal]
            }
          ]
        };

        this.options = {
          legend: {
            display: true
          },
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            xAxes: [
              {
                display: true,
                gridLines: {
                  display: false
                }
              }],
            yAxes: [
              {
                display: true,
                gridLines: {
                  display: false
                }
              }]
          }
        }

    });
  }


}






