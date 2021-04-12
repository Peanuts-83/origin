-- Test sur 3 procedures : la table / la vue / la vue matérialisée
-- Avec résultat en ms

-- Test sur la table
DELIMITER |
CREATE PROCEDURE test_perf_table()
BEGIN
    -- DECLARE var loc pr boucle 1000 fois et prise en cpte des données
    DECLARE v_max INT DEFAULT 1000;     -- boucle 1000 fois
    DECLARE v_min INT DEFAULT 0;        -- pt de départ
    DECLARE v_id INT(4);                -- espece_id
    DECLARE v_sum DECIMAL(15,2);        -- SUM(Adoption.prix) as somme
    DECLARE v_count INT;                -- COUNT(Animal.id) as nbr
    DECLARE v_year CHAR(4);             -- YEAR(date_reservation) as year

    boucle: LOOP
        -- Conditions de sortie de LOOP
        IF v_min = v_max THEN
            LEAVE boucle;
        END IF;

        -- Table
        SELECT SQL_NO_CACHE espece_id, 
        SUM(Adoption.prix) as somme, 
        COUNT(Animal.id) as nbr, 
        YEAR(date_reservation) as year
        INTO v_id, v_sum, v_count, v_year
        FROM Adoption
        JOIN Animal ON Adoption.animal_id=Animal.id
        JOIN Espece ON Animal.espece_id=Espece.id
        WHERE espece_id = 2
        GROUP BY year, Espece.id
        ORDER BY somme DESC
        LIMIT 1;

        SET v_min = v_min + 1;
    END LOOP;
END |
DELIMITER ;

-- Test sur la vue V_Revenus_annee_esp
DELIMITER |
CREATE PROCEDURE test_perf_Vue()
BEGIN
    -- DECLARE var loc pr boucle 1000 fois et prise en cpte des données
    DECLARE v_max INT DEFAULT 1000;     -- boucle 1000 fois
    DECLARE v_min INT DEFAULT 0;        -- pt de départ
    DECLARE v_id INT(4);                -- espece_id
    DECLARE v_sum DECIMAL(15,2);        -- SUM(Adoption.prix) as somme
    DECLARE v_count INT;                -- COUNT(Animal.id) as nbr
    DECLARE v_year CHAR(4);             -- YEAR(date_reservation) as year

    boucle: LOOP
        -- Conditions de sortie de LOOP
        IF v_min = v_max THEN
            LEAVE boucle;
        END IF;

        -- Table
        SELECT SQL_NO_CACHE espece_id, somme, nbr, year
        INTO v_id, v_sum, v_count, v_year
        FROM V_Revenus_annee_esp
        WHERE espece_id = 2
        ORDER BY somme DESC
        LIMIT 1;

        SET v_min = v_min + 1;
    END LOOP;
END |
DELIMITER ;

-- Test sur la vue matérialisée VM_Revenus_annee_esp
DELIMITER |
CREATE PROCEDURE test_perf_VM()
BEGIN
    -- DECLARE var loc pr boucle 1000 fois et prise en cpte des données
    DECLARE v_max INT DEFAULT 1000;     -- boucle 1000 fois
    DECLARE v_min INT DEFAULT 0;        -- pt de départ
    DECLARE v_id INT(4);                -- espece_id
    DECLARE v_sum DECIMAL(15,2);        -- SUM(Adoption.prix) as somme
    DECLARE v_count INT;                -- COUNT(Animal.id) as nbr
    DECLARE v_year CHAR(4);             -- YEAR(date_reservation) as year

    boucle: LOOP
        -- Conditions de sortie de LOOP
        IF v_min = v_max THEN
            LEAVE boucle;
        END IF;

        -- Table
        SELECT SQL_NO_CACHE espece_id, somme, nbr, year
        INTO v_id, v_sum, v_count, v_year
        FROM VM_Revenus_annee_esp
        WHERE espece_id = 2
        ORDER BY somme DESC
        LIMIT 1;

        SET v_min = v_min + 1;
    END LOOP;
END |
DELIMITER ;


-- Appel des 3 procedures
CALL test_perf_table();     -- 0.12 sec
CALL test_perf_Vue();       -- 0.14 sec
CALL test_perf_VM();        -- 0.05 sec
