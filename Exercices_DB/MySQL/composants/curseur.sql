-- CURSEUR / récupérer une suite de resultats d'un SELECT avec FETCH, une boucle LOOP et un HANDLER
DELIMITER |
CREATE PROCEDURE test_condition(IN p_ville VARCHAR(100))
BEGIN
    DECLARE v_nom, v_prenom VARCHAR(100);               -- variables locales
    DECLARE fin TINYINT DEFAULT 0;                      -- variable locale fin de boucle (BOOL/BOOLEAN)
    DECLARE curs_client CURSOR                          -- CURSOR recherche habitants d'une ville donnée
    FOR SELECT nom, prenom FROM Client WHERE ville=p_ville;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET fin=1;   -- Gestionnaire erreur NOT FOUND
    
    OPEN curs_client;                                   -- ouverture CURSOR
    loop_curs : LOOP                                    -- ouverture LOOP
        FETCH curs_client INTO v_nom, v_prenom;         -- FETCH results
        IF fin=1 THEN                                   -- IF QUIT LOOP
            LEAVE loop_curs;
        END IF;
        SELECT CONCAT_ws(' ',v_prenom,v_nom) as 'habitant(e)';           -- SELECT results
    END LOOP;                                           -- fermeture LOOP
    CLOSE curs_client;  	                            -- fermeture CURSOR
END |
DELIMITER ;

-------------------------------------
-- WHILE / Boucle alternative

    OPEN curs_client;
    WHILE fin=0 DO
        FETCH curs_client INTO v_nom, v_prenom;
        SELECT CONCAT(v_prenom,' ',v_nom);
    END WHILE;
    CLOSE curs_client;

-------------------------------------
-- REPEAT / Boucle alternative 2

    OPEN curs_client;
    REPEAT
        FETCH curs_client INTO v_nom, v_prenom;
        SELECT CONCAT_WS(' ',v_prenom,v_nom);
        UNTIL fin;                                      -- fin is true (1 en mysql)
    END REPEAT;
    CLOSE curs_client;

-- Appel test_condition
CALL test_condition('Belville');


-------------------------------------
-- Preparer une requête dans un SELECT
DELIMITER |
CREATE PROCEDURE select_race_dyn(p_clause VARCHAR(255))
BEGIN
    SET @sql = CONCAT('SELECT nom, description FROM RACE ', p_clause);
    -- REQUETE PREPAREE
    PREPARE requete FROM @sql;
    EXECUTE requete;
END|
DELIMITER ;

-- Appel descriptions chats
CALL select_race_dyn('WHERE espece_id=2');
-- Appel description 2 premieres races par ordre alphabetique
CALL select_race_dyn('ORDER BY nom LIMIT 2');
