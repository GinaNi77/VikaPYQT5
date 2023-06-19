procedures = """
CREATE PROCEDURE calculate_payment_cost()
BEGIN
    SET SQL_SAFE_UPDATES = 0;
    UPDATE payment p
    SET costPayment = (
    SELECT oc.costOrderCard + COALESCE(SUM(iw.costWork), 0)
    FROM ordercard oc
    LEFT JOIN installationwork iw ON oc.idOrderCard = iw.idOrderCard
    WHERE p.idOrderCard = oc.idOrderCard
    GROUP BY oc.idOrderCard
    );
    SET SQL_SAFE_UPDATES = 1;
END;

CREATE PROCEDURE calculate_ordercard_cost()
BEGIN
    SET SQL_SAFE_UPDATES = 0;
	UPDATE ordercard oc
	
	SET costOrderCard = (
		SELECT SUM(costOrder)
		FROM `order` o
		WHERE o.idOrderCard = oc.idOrderCard
	);
	SET SQL_SAFE_UPDATES = 1;
END;
"""