-- Historique heavy / TRIGGER TABLE Animal avec TABLE Animal_histo
-- Création table
CREATE TABLE Animal_histo (
    -- colonnes historisées
    id SMALLINT(6) UNSIGNED NOT NULL,
    sexe CHAR(1),
    date_naissance DATETIME NOT NULL,
    nom varchar(30),
    commentaires TEXT,
    espece_id SMALLINT(6) UNSIGNED NOT NULL,
    race_id SMALLINT(6) UNSIGNED DEFAULT NULL,
    mere_id SMALLINT(6) UNSIGNED DEFAULT NULL,
    pere_id SMALLINT(6) UNSIGNED DEFAULT NULL,
    dispo BOOL DEFAULT TRUE,

    -- colonnes techniques
    date_histo DATETIME NOT NULL,
    utilisateur_histo VARCHAR(20) NOT NULL,
    evenement_histo CHAR(6) NOT NULL,

    PRIMARY KEY (id, date_histo)
) ENGINE=InnoDB;

-- TRIGGER UPDATE/DELETE Animal
DELIMITER |
CREATE TRIGGER after_update_animal AFTER UPDATE ON Animal FOR EACH ROW
BEGIN
    INSERT INTO Animal_histo (id, sexe, date_naissance, nom, commentaires, espece_id, race_id, mere_id, pere_id, dispo, date_histo, utilisateur_histo, evenement_histo)
    VALUES ( OLD.id, OLD.sexe, OLD.date_naissance, OLD.nom, OLD.commentaires, OLD.espece_id, OLD.race_id, OLD.mere_id, OLD.pere_id, OLD.dispo, NOW(), CURRENT_USER(), 'UPDATE');
END |

CREATE TRIGGER after_delete_animal AFTER DELETE ON Animal FOR EACH ROW
BEGIN
    INSERT INTO Animal_histo (id, sexe, date_naissance, nom, commentaires, espece_id, race_id, mere_id, pere_id, dispo, date_histo, utilisateur_histo, evenement_histo)
    VALUES ( OLD.id, OLD.sexe, OLD.date_naissance, OLD.nom, OLD.commentaires, OLD.espece_id, OLD.race_id, OLD.mere_id, OLD.pere_id, OLD.dispo, NOW(), CURRENT_USER(), 'DELETE');
END |
DELIMITER ;

-- Test historique Heavy
UPDATE Animal
SET commentaires = 'Petit pour son âge'
WHERE id = 10;

DELETE FROM Animal
WHERE id = 47;

SELECT id, sexe, date_naissance, nom, commentaires, espece_id
FROM Animal 
WHERE id IN (10, 47);

SELECT id, nom, date_histo, utilisateur_histo, evenement_histo 
FROM Animal_histo;

-- Clés étrangères
-- Une suppression ou modification de données déclenchée par une clé étrangère ne provoquera pas l'exécution du trigger correspondant.
-- Suppression des 4 clés étrangères posant problème
ALTER TABLE Animal DROP FOREIGN KEY fk_mere_id,
                    DROP FOREIGN KEY fk_pere_id,
                    DROP FOREIGN KEY fk_race_id;
ALTER TABLE Race DROP FOREIGN KEY fk_race_espece_id;

-- Re-création des clés sans les options ON DELETE SET NULL/ CASCADE
ALTER TABLE Animal
    ADD CONSTRAINT fk_mere_id FOREIGN KEY (mere_id) REFERENCES Animal(id),
    ADD CONSTRAINT fk_pere_id FOREIGN KEY (pere_id) REFERENCES Animal(id),
    ADD CONSTRAINT fk_race_id FOREIGN KEY (race_id) REFERENCES Race(id);
ALTER TABLE Race
    ADD CONSTRAINT fk_race_espece_id FOREIGN KEY (espece_id) REFERENCES Espece(id);

-- TRIGGER sur Race
CREATE TRIGGER before_delete_race BEFORE DELETE ON Race FOR EACH ROW
UPDATE Animal SET race_id=NULL WHERE race_id=OLD.id;

-- TRIGGER sur Espece
CREATE TRIGGER before_delete_espece BEFORE DELETE ON Espece FOR EACH ROW
UPDATE Animal SET espece_id=NULL WHERE espece_id=OLD.id;
