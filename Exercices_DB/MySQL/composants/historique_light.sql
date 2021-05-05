-- Historique basique / TRIGGER - Dans TABLE Race
-- modif° TABLE Race
ALTER TABLE Race 
    ADD COLUMN date_insertion DATETIME,
    ADD COLUMN utilisateur_insertion VARCHAR(20),
    ADD COLUMN date_modification DATETIME,
    ADD COLUMN utilisateur_modification VARCHAR(20);

-- remplissage col
UPDATE Race 
SET date_insertion= NOW() - INTERVAL 1 DAY,
    utilisateur_insertion= 'Test',
    date_modification= NOW() - INTERVAL 1 DAY,
    utilisateur_modification= 'Test';

-- TRIGGER INSERT/UPDATE Race
DELIMITER |
CREATE TRIGGER before_insert_race BEFORE INSERT
ON Race FOR EACH ROW
BEGIN
    SET NEW.date_insertion= NOW();
    SET NEW.utilisateur_insertion= CURRENT_USER();
    SET NEW.date_modification= NOW();
    SET NEW.utilisateur_modification= CURRENT_USER();
END |

CREATE TRIGGER before_update_race BEFORE UPDATE
ON Race FOR EACH ROW
BEGIN
    SET NEW.date_modification= NOW();
    SET NEW.utilisateur_modification= CURRENT_USER();
END |
DELIMITER ;

-- Test TRIGGER TABLE Race
INSERT INTO Race (nom, description, espece_id, prix)
VALUES ('Yorkshire terrier', 'Chien de petite taille au pelage long et soyeux de couleur bleu et feu.', 1, 700.00);

UPDATE Race 
SET prix = 630.00 
WHERE nom = 'Rottweiller' AND espece_id = 1;

SELECT nom, DATE(date_insertion) AS date_ins, utilisateur_insertion AS utilisateur_ins, DATE(date_modification) AS date_mod, utilisateur_modification AS utilisateur_mod 
FROM Race 
WHERE espece_id = 1;