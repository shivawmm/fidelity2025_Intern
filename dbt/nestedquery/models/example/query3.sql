SELECT  
    c.customerNumber AS customer_id,  
    c.customerName,  
    o.orderNumber,  
    o.status,  
    p.productName 
FROM  
    fidelity.customers AS c  
JOIN  
    fidelity.orders AS o  
ON  
    c.customerNumber = o.customerNumber  
JOIN  
    fidelity.orderdetails AS od  
ON  
    o.orderNumber = od.orderNumber  
JOIN  
    fidelity.products AS p  
ON  
    od.productCode = p.productCode
