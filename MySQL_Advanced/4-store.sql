-- Trigger that decreases quauntity of items when an order is placed, essentially.
DROP TRIGGER IF EXISTS decrease_quantity;

CREATE TRIGGER decrease_quantity
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;