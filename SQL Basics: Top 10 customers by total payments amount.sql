SELECT customer.customer_id, email, count(payment_id) as payments_count, sum(amount)::float as total_amount
FROM customer
JOIN payment on customer.customer_id=payment.customer_id
Group BY customer.customer_id
ORDER by total_amount DESC
LIMIT 10
