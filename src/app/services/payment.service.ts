import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PaymentService {
  private apiUrl = 'http://127.0.0.1:8000/api/payments';

  constructor(private http: HttpClient) {}

  // Fetch all payments
  getPayments(): Observable<any> {
    return this.http.get(this.apiUrl);
  }

  // Create a new payment
  createPayment(paymentData: any): Observable<any> {
    return this.http.post(this.apiUrl, paymentData);
  }

  // Update a payment
  updatePayment(id: string, updates: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/${id}`, updates);
  }

  // Delete a payment
  deletePayment(id: string): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`);
  }
}
