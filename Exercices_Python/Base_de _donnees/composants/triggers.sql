-- TRIGGER / INSERT & UPDATE sexe : 'M'/'F'
DELIMITER |
CREATE TRIGGER before_insert_sexe BEFORE INSERT
ON Animal FOR EACH ROW
BEGIN
    IF NEW.sexe IS NOT NULL AND NEW.sexe != 'M' AND NEW.sexe != 'F' THEN
        -- sexe = NULL si mauvaise valeur
        -- SET NEW.sexe = NULL;
        -- sexe déclenche erreur liée à table Erreur (INSERT d'une erreur UNIQUE déjà entrée)
        INSERT INTO Erreur (erreur) VALUES('Erreur: sexe doit être ''F''|''M''|NULL');
    END IF;
END |

CREATE TRIGGER before_update_sexe BEFORE UPDATE
ON Animal FOR EACH ROW
BEGIN
    IF NEW.sexe IS NOT NULL AND NEW.sexe != 'M' AND NEW.sexe != 'F' THEN
        -- sexe = NULL si mauvaise valeur
        -- SET NEW.sexe = NULL;
        -- sexe déclenche erreur liée à table Erreur (INSERT d'une erreur UNIQUE déjà entrée)
        INSERT INTO Erreur (erreur) VALUES('Erreur: sexe doit être ''F''|''M''|NULL');
    END IF;
END |
DELIMITER ;


-- TRIGGER / INSERT & UPDATE paye : 0/1
DELIMITER |
CREATE TRIGGER before_insert_paye BEFORE INSERT
ON Adoption FOR EACH ROW
BEGIN
    IF NEW.paye != 0 AND NEW.paye != 1 THEN
        INSERT INTO Erreur (erreur) VALUES('Erreur: paye doit être TRUE(1)|FALSE(0)');
    END IF;
END |

CREATE TRIGGER before_update_paye BEFORE UPDATE
ON Adoption FOR EACH ROW
BEGIN
    IF NEW.paye != 0 AND NEW.paye != 1 THEN
        INSERT INTO Erreur (erreur) VALUES('Erreur: paye doit être TRUE(1)|FALSE(0)');
    END IF;
END |
DELIMITER ;


-- TRIGGER / INSERT & UPDATE date_adoption (>= date_reservation)
DELIMITER |
CREATE TRIGGER before_insert_date_adoption BEFORE INSERT
ON Adoption FOR EACH ROW
BEGIN
    IF NEW.date_adoption < NEW.date_reservation THEN
        INSERT INTO Erreur (erreur) VALUES('Erreur: la date d''adoption doit être postérieure ou égale à celle de réservation');
    END IF;
END |

CREATE TRIGGER before_update_date_adoption BEFORE UPDATE
ON Adoption FOR EACH ROW
BEGIN
    IF NEW.date_adoption < NEW.date_reservation THEN
        INSERT INTO Erreur (erreur) VALUES('Erreur: la date d''adoption doit être postérieure ou égale à celle de réservation');
    END IF;
END |
DELIMITER ;


-- TRIGGER disponibilité animal -- 
-- ajout col DISPO dans Animal
ALTER TABLE Animal ADD COLUMN dispo BOOL DEFAULT TRUE;

-- remplissage col DISPO
UPDATE Animal SET dispo=FALSE WHERE EXISTS (SELECT * FROM Adoption WHERE Animal.id=Adoption.animal_id); 

-- TRIGGER INSERT/UPDATE/DELETE Adoption
DELIMITER |
CREATE TRIGGER after_insert_adoption AFTER INSERT
ON Adoption FOR EACH ROW
BEGIN
    UPDATE Animal SET dispo=FALSE WHERE id=NEW.animal_id;
END |

CREATE TRIGGER after_update_adoption AFTER UPDATE
ON Adoption FOR EACH ROW
BEGIN
    IF NEW.animal_id != OLD.animal_id THEN
        UPDATE Animal SET dispo=TRUE WHERE id=OLD.animal_id;
        UPDATE Animal SET dispo=FALSE WHERE id=NEW.animal_id;
    END IF;
END |

CREATE TRIGGER after_delete_adoption AfTER DELETE
ON Adoption FOR EACH ROW
BEGIN
    UPDATE Animal SET dispo=TRUE WHERE id=OLD.animal_id;
END |
DELIMITER ;
