-- VM / Vue matérialisée de VIEW V_Revenus_anne_esp / Données stockées dans une table (MySQL)
CREATE TABLE VM_Revenus_annee_esp
Engine=InnoDB
SELECT espece_id, SUM(Adoption.prix) as somme, COUNT(Animal.id) as nbr, YEAR(date_reservation) as year
FROM Adoption
JOIN Animal ON Adoption.animal_id=Animal.id
JOIN Espece ON Animal.espece_id=Espece.id
GROUP BY year, Espece.id;

-- Gestion des MAJ / ON DEMAND ou AUTO
-- ON DEMAND / Via PROCEDURE STOCKEE
DELIMITER |
CREATE PROCEDURE maj_vm_revenus()
BEGIN
    TRUNCATE VM_Revenus_annee_esp;          -- TRUNCATE = DELETE + rapide (suppr Table puis recréée vide)
    INSERT INTO VM_Revenus_annee_esp 
    SELECT nom_courant, SUM(Adoption.prix) as somme, COUNT(Animal.id) as nbr, YEAR(date_reservation) as year
    FROM Adoption
    JOIN Animal ON Adoption.animal_id=Animal.id
    JOIN Espece ON Animal.espece_id=Espece.id
    GROUP BY year, nom_courant;
END |
DELIMITER ;
--Appel MAJ
CALL maj_vm_revenus();

-- Contrainte si chgt dans TABLE Espece
ALTER TABLE VM_Revenus_annee_esp
    ADD CONSTRAINT fk_vm_revenus_esp_id FOREIGN KEY (espece_id) REFERENCES Espece(id) ON DELETE CASCADE,
    ADD PRIMARY KEY (year, espece_id);

-- AUTO / Via TRIGGERS qui détectent modifications données des TABLES concernées
-- Modification TRIGGER INSERT/UPDATE/DELETE Adoption

DELIMITER |
DROP TRIGGER after_insert_adoption|
CREATE TRIGGER after_insert_adoption AFTER INSERT
ON Adoption FOR EACH ROW
BEGIN
    UPDATE Animal SET disponible=FALSE WHERE id=NEW.animal_id;
    
    INSERT INTO VM_Revenus_annee_esp (espece_id, somme, nbr, year)
    SELECT espece_id, NEW.prix, 1, YEAR(NEW.date_reservation)
    FROM Animal
    WHERE id = NEW.animal_id
    ON DUPLICATE KEY UPDATE somme = somme + NEW.prix, nbr = nbr + 1;
END |

DROP TRIGGER after_update_adoption|
CREATE TRIGGER after_update_adoption AFTER UPDATE
ON Adoption FOR EACH ROW
BEGIN
    IF OLD.animal_id != NEW.animal_id THEN
        UPDATE Animal SET disponible=FALSE WHERE id=NEW.animal_id;
        UPDATE Animal SET disponible=TRUE WHERE id=OLD.animal_id;
    END IF;

    INSERT INTO VM_Revenus_annee_esp (espece_id, somme, nbr, year)
    SELECT espece_id, NEW.prix, 1, YEAR(NEW.date_reservation)
    FROM Animal
    WHERE id = NEW.animal_id
    ON DUPLICATE KEY UPDATE somme = somme + NEW.prix, nbr = nbr + 1;

    UPDATE VM_Revenus_annee_esp SET somme = somme - OLD.prix, nbr = nbr - 1 
    WHERE year = YEAR(OLD.date_reservation)
    AND espece_id = (SELECT espece_id FROM Animal WHERE id=OLD.animal_id);

    DELETE FROM VM_Revenus_annee_esp WHERE nbr=0;
END |

DROP TRIGGER after_delete_adoption|
CREATE TRIGGER after_delete_adoption AFTER DELETE
ON Adoption FOR EACH ROW
BEGIN
    UPDATE Animal SET disponible=TRUE WHERE id=OLD.animal_id;

    UPDATE VM_Revenus_annee_esp SET somme = somme - OLD.prix, nbr = nbr - 1
    WHERE year = YEAR(OLD_date_reservation)
    AND espece_id = (SELECT espece_id FROM Animal WHERE id=OLD.animal_id);

    DELETE FROM VM_Revenus_annee_esp WHERE nbr=0;
END |
DELIMITER ;
