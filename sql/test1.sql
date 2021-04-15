ALTER TABLE order
ADD status varchar2(25);

declare 
CURSOR liste_ordre is select* FROM order;
ligne liste_ordre%ROWTYPE;
begin
	for ligne in liste_services LOOP
		if O.order_delivered is not NULL then 
			update order set status="delivered";
		elsif O.order_shipped is not null THEN
			update order set status="shipped";
		elsif O.order_prepared is not null THEN
			update order set status="prepared";
		elsif O.payment_received is not null THEN
			update order set status="paid";
		else update order set status="received";
		end if;
	end loop;
	SELECT U.id as UserID,U.first_name as prenom,U.last_name,status as nom FROM user U join order O on O.user_id=U.user_id where (O.id >1336 and O.id <1501) order by (last_name) desc;

end;