
ALTER TABLE order
ADD year integer;

update order set year=substr(order_received,1,4);
	
select O.year as year, count(DISTINCT O.id) as ordercount,count(L.id) as linecount from order O join order_line L on O.id=L.order_id group by (O.year) ;
