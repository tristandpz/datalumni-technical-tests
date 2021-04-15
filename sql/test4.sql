
select U.id,last_name,first_name from user U join 
(order O join order_line L on O.id=L.order_id)on O.user_id=U.id group by U.id,O.year
order by (sum(quantity*unit_price)) desc limit 10;

--On considère que le changement de la table order faites au tests 2 à déjà été fait
-- Je n'arrive pas à faire donner le rang par année, j'ai seulement réussit à classer les 10 plus gros CA sur toutes les années.


