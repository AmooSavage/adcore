import { Component, OnInit } from '@angular/core';
import { PaymentService } from '../../services/payment.service';  // Adjust path as needed

@Component({
  selector: 'app-payment-list',
  templateUrl: './payment-list.component.html',
  styleUrls: ['./payment-list.component.scss']  // Use .scss extension for SCSS
})
export class PaymentListComponent implements OnInit {
  payments: any[] = [];
  errorMessage: string = '';

  constructor(private paymentService: PaymentService) { }

  ngOnInit(): void {
    this.fetchPayments();
  }

  fetchPayments(): void {
    this.paymentService.getPayments().subscribe(
      (data) => {
        this.payments = data.payments;
      },
      (error) => {
        console.error('Error fetching payments:', error);
        this.errorMessage = 'Failed to fetch payments. Please try again.';
      }
    );
  }

  deletePayment(id: string): void {
    this.paymentService.deletePayment(id).subscribe(
      () => {
        console.log('Payment deleted successfully');
        // Optionally, refresh payments list after deletion:
        this.fetchPayments();
      },
      (error) => {
        console.error('Error deleting payment:', error);
        this.errorMessage = 'Failed to delete the payment. Please try again.';
      }
    );
  }
}
