SELECT 
    product_id,
    transaction_id

FROM 
    fidelity.sales_db
WHERE
    product_id IS NOT NULL
    AND transaction_id IS NOT NULL