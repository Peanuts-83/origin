-- CREATE USER / % for joker
CREATE USER 'tester'@'localhost' IDENTIFIED BY 'passtest';
CREATE USER 'tester'@'188.167.23.%' IDENTIFIED BY 'passtest';
CREATE USER 'tester2'@'%' IDENTIFIED BY 'passtest2';              -- connection from anywhere!

-- Modifications
RENAME USER 'tester2'@'%' TO 'tester222'@'localhost';
ALTER USER 'tester222'@'localhost' IDENTIFIED BY 'passtest222';

-- DROP USER
DROP USER 'tester222'@'localhost';

-- GRANT PRIVILEGES
GRANT ALL PRIVILEGES            -- ALL (sauf GRANT -> WITH GRANT OPTION;)
ON test.*
TO 'peanuts'@'localhost';

GRANT ROUTINE, EXECUTE
ON Test.*
TO 'tester'@'localhost';

GRANT SELECT,
    UPDATE (nom,sexe,commentaires),
    DELETE,
    INSERT
ON TABLE ElevagE.Animal
TO 'tester'@'localhost';

-- REVOKE PRIVILEGES
REVOKE INSERT ON TABLE ElevagE.Animal TO 'tester222'@'%';

