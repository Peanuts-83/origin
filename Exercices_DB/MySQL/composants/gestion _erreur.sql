-- EXIT HANDLER / les instr° sont exécutées si erreur corresp au gestionnaire. / PROC stop
DELIMITER |
CREATE PROCEDURE ajout_adoption_exit(IN p_client_id INT, IN p_animal_id INT, IN p_date DATE, IN p_paye TINYINT)
BEGIN   
    DECLARE v_prix DECIMAL(7,2);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION       -- gestionnaire d'erreur avec EXIT
        BEGIN                                   -- stop a toute erreur SQL
            SELECT 'Error occured...';
            SELECT 'End of procedure!';
        END;

    SELECT 'Procedure starting';

    SELECT COALESCE(Race.prix, Espece.prix) INTO v_prix
    FROM Animal
    JOIN Espece ON Animal.espece_id=Espece.id
    LEFT JOIN Race ON Animal.race_id=Race.id
    WHERE Animal.id=p_animal_id;
    
    INSERT INTO Adoption (animal_id, client_id, date_reservation, date_adoption, prix, paye)
    VALUES (p_animal_id, p_client_id, DATE(NOW()), p_date, v_prix, p_paye);

    SELECT 'End of procedure.';
END|
DELIMITER ;

-- Appel procedure
SET @date_adoption = DATE(NOW()) + INTERVAL 7 DAY;
CALL ajout_adoption_exit(18,6,@date_adoption,1);


---------------------------------------
-- CONTINUE HANDLER / PROC continue
DELIMITER |
CREATE PROCEDURE ajout_adoption_continue(IN p_client_id INT, IN p_animal_id INT, IN p_date DATE, IN p_paye TINYINT)
BEGIN
    DECLARE v_prix DECIMAL(7,2);
    DECLARE CONTINUE HANDLER FOR SQLSTATE '23000'   -- gestionnaire d'erreur avec CONTINUE
    BEGIN                                           -- 23000 = Violation contrainte unicité/clée sec/col not null
        SELECT 'Error occured...';
        SELECT 'Still running!';
    END;

    SELECT COALESCE(Race.prix, Espece.prix) INTO v_prix
    FROM Animal
    JOIN Espece ON Animal.espece_id=Espece.id
    LEFT JOIN Race ON Animal.race_id=Race.id
    WHERE Animal.id=p_animal_id;
    
    INSERT INTO Adoption (animal_id, client_id, date_reservation, date_adoption, prix, paye)
    VALUES (p_animal_id, p_client_id, DATE(NOW()), p_date, v_prix, p_paye);

    SELECT 'End of procedure.';
END|
DELIMITER ;

-- Appel procedure
SET @date_adoption = DATE(NOW()) + INTERVAL 7 DAY;
CALL ajout_adoption_continue(18,6,@date_adoption,1);


-------------------------------------
-- Multiples HANDLER et CONDITION FOR (HANDLER)
DROP PROCEDURE ajout_adoption_exit;
DELIMITER |
CREATE PROCEDURE ajout_adoption_exit(IN p_client_id INT, IN p_animal_id INT, IN p_date DATE, IN p_paye TINYINT)
BEGIN
    DECLARE v_prix DECIMAL(7,2);
    -- GESTIONNAIRE D'ERREUR --
    -- Creation des CONDITIONS (Alias d'erreur)
    DECLARE violation_clee_etrangere CONDITION FOR 1452;    -- 1452 = MySQL error / cond 1 avec alias
    DECLARE violation_unicite CONDITION FOR 1062;           -- 1062 = MySQL error / cond 2 avec alias
    -- Déclaration cond 1
    DECLARE EXIT HANDLER FOR violation_clee_etrangere
    BEGIN   
        SELECT 'Erreur: violation de clée étrangère';
    END;
    -- Déclaration cond 2
    DECLARE EXIT HANDLER FOR violation_unicite
    BEGIN
        SELECT 'Erreur, violation d''unicité';
    END;
    -- FIN GESTIONNAIRE D'ERREUR --

    -- DEBUT PROCEDURE --
    SELECT 'Procedure starting';
    SELECT COALESCE(Race.prix, Espece.prix) INTO v_prix     -- attribue valeur à var loc v_prix
    FROM Animal
    JOIN Espece ON Animal.espece_id=Espece.id
    LEFT JOIN Race ON Animal.race_id=Race.id
    WHERE Animal.id=p_animal_id;

    INSERT INTO Adoption (client_id, animal_id, date_reservation, date_adoption, prix, paye)
    VALUES (p_client_id, p_animal_id, DATE(NOW()), p_date, v_prix, p_paye);
    SELECT 'End of procedure';
END|
DELIMITER ;

-- Appel procedure avec multiples HANDLERS
SET @date_adoption = CURRENT_DATE() + INTERVAL 7 DAY;

CALL ajout_adoption_exit(12, 3, @date_adoption, 1);        
-- Violation unicité (animal 3 est déjà adopté)
CALL ajout_adoption_exit(133, 6, @date_adoption, 1);       
-- Violation clé étrangère (client 133 n'existe pas)
CALL ajout_adoption_exit(NULL, 6, @date_adoption, 1);      
-- Violation de contrainte NOT NULL


------------------------------------------------------
-- TRANSACTION & GESTIONNAIRE D'ERREUR / ROLLBACK en cas d'échec d'une des requêtes
DELIMITER |
CREATE PROCEDURE adopt_2_ou_rien(IN p_client_id INT, IN p_animal_id1 INT, IN p_animal_id2 INT)
BEGIN
    DECLARE v_prix DECIMAL(7,2);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SELECT 'Error occured during process, changes invalidated.' as message;
        ROLLBACK;
    END;

    START TRANSACTION;
        -- Adoption animal 1
        SELECT COALESCE(Race.prix, Espece.prix) INTO v_prix
        FROM Animal
        JOIN Espece ON Animal.espece_id=Espece.id
        LEFT JOIN Race ON Animal.race_id=Race.id
        WHERE Animal.id=p_animal_id1;
        INSERT INTO Adoption (client_id, animal_id, date_reservation, date_adoption, prix, paye)
        VALUES (p_client_id, p_animal_id1, CURRENT_DATE(), @date_adoption, v_prix, 1);
        SELECT 'Adoption 1 ok' as message;
        
        -- Adoption animal 2
        SELECT COALESCE(Race.prix, Espece.prix) INTO v_prix
        FROM Animal
        JOIN Espece ON Animal.espece_id=Espece.id
        LEFT JOIN Race ON Animal.race_id=Race.id
        WHERE Animal.id=p_animal_id2;
        INSERT INTO Adoption (client_id, animal_id, date_reservation, date_adoption, prix, paye)
        VALUES (p_client_id, p_animal_id2, CURRENT_DATE(), @date_adoption, v_prix, 1);
        SELECT 'Adoption 2 ok' as message;
    COMMIT;
END|
DELIMITER ;

-- Appel adoption 2 animaux
SET @date_adoption = CURRENT_DATE() + INTERVAL 7 DAY;
CALL adopt_2_ou_rien(2,35,55);