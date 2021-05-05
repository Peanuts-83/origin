-- Conditions / IF
DELIMITER |
CREATE PROCEDURE est_adopte(IN p_animal_id INT)
BEGIN
    DECLARE v_nb INT DEFAULT 0;
    SELECT COUNT(*) INTO v_nb FROM Adoption
    WHERE animal_id=p_animal_id;

    IF v_nb>0 THEN
        SELECT 'Animal déjà adopté!' as alerte;
    END IF;
END |
DELIMITER ;

-- Appel procédure conditionnelle
CALL est_adopte(3);
CALL est_adopte(28);

--------------------------------------
-- Conditions / IF - ELSE IF - ELSE
DELIMITER |
CREATE PROCEDURE message_sexe(IN p_animal_id INT)
BEGIN
    DECLARE v_sexe VARCHAR(10);

    SELECT sexe INTO v_sexe
    FROM Animal
    WHERE id = p_animal_id;

    IF (v_sexe = 'F') THEN      -- Première possibilité
        SELECT 'Je suis une femelle !' AS sexe;
    ELSEIF (v_sexe = 'M') THEN  -- Deuxième possibilité
        SELECT 'Je suis un mâle !' AS sexe;
    ELSE                        -- Défaut
        BEGIN                   -- pas d'instruction
        END;
    END IF;
END|
DELIMITER ;

-- Appel condition 2 
CALL message_sexe(8);   -- Mâle
CALL message_sexe(6);   -- Femelle
CALL message_sexe(9);   -- Ni l'un ni l'autre

-------------------------------------
-- Conditions / CASE
DROP PROCEDURE salut_nom;
DELIMITER |
CREATE PROCEDURE salut_nom(IN p_animal_id INT)
BEGIN
    DECLARE v_terminaison CHAR(1);

    SELECT SUBSTRING(nom, -1, 1) INTO v_terminaison
    FROM Animal
    WHERE id = p_animal_id;

    CASE v_terminaison
        WHEN 'a' THEN
            SELECT 'Bonjour !' AS Salutations;
        WHEN 'o' THEN
            SELECT 'Salut !' AS Salutations;
        WHEN 'i' THEN
            SELECT 'Coucou !' AS Salutations;
        ELSE
            BEGIN   -- Bloc d'instructions vide
            END;
    END CASE;

END|
DELIMITER ;

-- Appel condition 3
CALL salut_nom(69);  -- Baba
CALL salut_nom(5);   -- Choupi
CALL salut_nom(29);  -- Fiero
CALL salut_nom(54);  -- Bubulle

---------------------------------------
-- CASE dans une requete
SELECT id, nom, CASE
          WHEN sexe = 'M' THEN 'Je suis un mâle !'
          WHEN sexe = 'F' THEN 'Je suis une femelle !'
          ELSE 'Je suis en plein questionnement existentiel...'
       END AS message
FROM Animal
WHERE id IN (9, 8, 6);

