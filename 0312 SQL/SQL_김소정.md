# SQL_김소정
1. 국가별 office와 employee의 수
```sql    
select country, count(distinct offices.officeCode) as office수, count(distinct employeeNumber) as employee수
from offices
left join employees on offices.officeCode = employees.officeCode
group by 1;
```
![](https://i.imgur.com/Fiknhet.png)
<br/>

2. cumtomerFirstName이 R로 시작하는 고객 리스트
```sql    
select customerName from customers
where contactFirstName like "R%";
```
![](https://i.imgur.com/Zlfl4EL.png)
<br/>



3. order 상태가 'Cancelled' 또는 'On Hold'인 미국 고객의 주문 건수
```sql    
select status, count(orderNumber) as 주문건수 from orders
left join customers on orders.customerNumber = customers.customerNumber
where country = "USA"
group by 1
Having status = 'Cancelled' or status = 'On Hold';
```
![](https://i.imgur.com/0wwkb17.png)
<br/>


4. 가장 많은 고객을 담당한 office code
```sql    
select officeCode from employees
left join customers on employees.employeeNumber = customers.salesRepEmployeeNumber
group by officeCode
having count(distinct customerNumber) = (select max(counted)
	from (
		select officeCode, count(customerNumber) as counted
		from employees
		left join customers on employees.employeeNumber = customers.salesRepEmployeeNumber
		group by officeCode) as counts);
```
![](https://i.imgur.com/UZ6W265.png)
</br>


5. 2004년 11월 가장 많은 금액을 결제한 고객의 정보
```sql    
select customerName, phone, city, state from customers
where customerName in (select customerName from customers
	left join orders on customers.customerNumber = orders.customerNumber
	left join payments on customers.customerNumber = payments.customerNumber
	where extract(year from orderDate) = 2004 and extract(month from orderDate) = 11
	group by 1
	having sum(amount) in (select max(summed) from (
		select customerName, sum(amount) as summed from customers
		left join orders on customers.customerNumber = orders.customerNumber
		left join payments on customers.customerNumber = payments.customerNumber
		where extract(year from orderDate) = 2004 and extract(month from orderDate) = 11
		group by 1) as sums));
```
![](https://i.imgur.com/ts3hSVG.png)
</br>


6. 2005년 1월의 orderDate와 shippedDate 사이 기간의 최대, 최소값
```sql    
select min(shippedDate-orderDate) as 최소소요일, max(shippedDate-orderDate) as 최대소요일 from orders
where extract(year from orderDate) = 2005 and extract(month from orderDate) = 1;
```
![](https://i.imgur.com/7n1Ojkb.png)
<br/>


7. 2004년 1년간 가장 많은 금액을 결제한 고객의 담당 employee 정보
```sql    
select distinct salesRepEmployeeNumber, lastName, firstName, email, jobTitle from customers
left join employees on customers.salesRepEmployeeNumber = employees.employeeNumber
where salesRepEmployeeNumber in (select salesRepEmployeeNumber from customers
		where customerName in (select customerName from customers
			left join orders on customers.customerNumber = orders.customerNumber
			left join payments on customers.customerNumber = payments.customerNumber
			left join employees on customers.salesRepEmployeeNumber = employees.employeeNumber
			where extract(year from orderDate) = 2004
			group by 1
			having sum(amount) in (select max(summed) from (
				select customerName, sum(amount) as summed from customers
				left join orders on customers.customerNumber = orders.customerNumber
				left join payments on customers.customerNumber = payments.customerNumber
				left join employees on customers.salesRepEmployeeNumber = employees.employeeNumber
				where extract(year from orderDate) = 2004
				group by 1) as sums)));
```
![](https://i.imgur.com/61G87cQ.png)

