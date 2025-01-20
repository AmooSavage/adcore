import { Component } from '@angular/core';
import { PaymentService } from '../../services/payment.service';

@Component({
  selector: 'app-payment-form',
  templateUrl: './payment-form.component.html',
  styleUrls: ['./payment-form.component.css']
})
export class PaymentFormComponent {
  paymentData = {
    payee_first_name: '',
    payee_last_name: '',
    payee_payment_status: 'pending',
    due_amount: 0,
    currency: 'USD'
  };

  constructor(private paymentService: PaymentService) { }

  submitPayment(): void {
    this.paymentService.createPayment(this.paymentData).subscribe(
      (response) => {
        alert('Payment created successfully!');
      },
      (error) => {
        console.error('Error creating payment', error);
      }
    );
  }
}
