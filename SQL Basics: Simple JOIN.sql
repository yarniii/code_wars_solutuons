-- Create your SELECT statement here
SELECT products.id, products.name, isbn, company_id, price, companies.name as company_name
FROM products
LEFT JOIN companies on companies.id=products.company_id
