-- requete préparée (session courante / ephemere) + ? + variables utilisateur
-- Sans paramètre
PREPARE select_race
FROM 'SELECT * FROM Race';

'-- Avec un paramètre
PREPARE select_client
FROM 'SELECT * FROM Client WHERE email = ?';

-- Avec deux paramètres
PREPARE select_adoption
FROM 'SELECT * FROM Adoption WHERE client_id = ? AND animal_id = ?';

'-- appel requete preparee
EXECUTE select_race;

SET @id = 3;    -- variable utilisateur
EXECUTE select_col_animal USING @id;

SET @client = 2;
EXECUTE select_adoption USING @client, @id;

SET @email = 'jean.dupont@email.com';
EXECUTE select_client USING @email;

-------------------------------------
-------------------------------------
-- declaration de procedure (permanente) + parametres (IN(default) / OUT / INOUT)
DELIMITER |
CREATE PROCEDURE calculer_prix(p_animal_id INT, INOUT p_prix DECIMAL(7,2))
BEGIN
    SELECT p_prix + COALESCE(Race.prix, Espece.prix) INTO p_prix
    FROM Animal
    JOIN Espece ON Animal.espece_id=Espece.id
    LEFT JOIN Race ON Animal.race_id=Race.id
    WHERE Animal.id=p_animal_id;
END|
DELIMITER ;

-- appel de procedure 
SET @prix = 0;                   -- On initialise @prix à 0

CALL calculer_prix (13, @prix);  -- Achat de Rouquine
SELECT @prix AS prix_intermediaire;

CALL calculer_prix (24, @prix);  -- Achat de Cartouche
SELECT @prix AS prix_intermediaire;

CALL calculer_prix (42, @prix);  -- Achat de Bilba
SELECT @prix AS prix_intermediaire;

CALL calculer_prix (75, @prix);  -- Achat de Mimi
SELECT @prix AS total;.

----------------------------------
----------------------------------
-- declaration de variable locale (perm)
DELIMITER |
CREATE PROCEDURE aujourdhui_demain ()
BEGIN
    DECLARE v_date DATE DEFAULT CURRENT_DATE();               
    -- On déclare une variable locale et on lui met une valeur par défaut

    SELECT DATE_FORMAT(v_date, '%W %e %M %Y') AS Aujourdhui;

    SET v_date = v_date + INTERVAL 1 DAY;                     
    -- On change la valeur de la variable locale
    SELECT DATE_FORMAT(v_date, '%W %e %M %Y') AS Demain;
END|
DELIMITER ;

-- Appel de procedure avec variable locale
CALL aujourdhui_demain();

