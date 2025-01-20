import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PaymentListComponent } from './components/payment-list/payment-list.component';

const routes: Routes = [
  { path: '', redirectTo: '/payments', pathMatch: 'full' }, // Redirect root to /payments
  { path: 'payments', component: PaymentListComponent },    // Route for payments
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule { }
