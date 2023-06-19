triggers = """
CREATE TRIGGER calculate_work_cost 
BEFORE INSERT ON installationwork
FOR EACH ROW
BEGIN
	DECLARE duration INT;
	SET duration = DATEDIFF(NEW.endDate, NEW.beginDate);
	SET NEW.costWork = duration * 1000;
END;

CREATE TRIGGER calculate_order_cost
BEFORE INSERT ON `order`
FOR EACH ROW
BEGIN
	DECLARE product_cost DECIMAL(10, 2);
	SELECT costProduct INTO product_cost
	FROM product
	WHERE idProduct = NEW.idProduct;
	SET NEW.costOrder = NEW.amount * product_cost;
END;
"""