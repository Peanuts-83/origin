-- --------------------------
-- CREATION DE  LA TABLE Race
-- --------------------------
CREATE TABLE Race (
    id SMALLINT UNSIGNED AUTO_INCREMENT,
    nom VARCHAR(40) NOT NULL,
    espece_id SMALLINT UNSIGNED NOT NULL,     -- pas de nom latin, mais une référence vers l'espèce
    description TEXT,
    PRIMARY KEY(id),
    CONSTRAINT fk_race_espece_id FOREIGN KEY (espece_id) REFERENCES Espece(id)  -- pour assurer l'intégrité de la référence
)
ENGINE = InnoDB;

-- -----------------------
-- REMPLISSAGE DE LA TABLE
-- -----------------------
INSERT INTO Race (nom, espece_id, description)
VALUES ('Berger allemand', 1, 'Chien sportif et élégant au pelage dense, noir-marron-fauve, noir ou gris.'),
('Berger blanc suisse', 1, 'Petit chien au corps compact, avec des pattes courtes mais bien proportionnées et au pelage tricolore ou bicolore.'),
('Boxer', 1, 'Chien de taille moyenne, au poil ras de couleur fauve ou bringé avec quelques marques blanches.'),
('Bleu russe', 2, 'Chat aux yeux verts et à la robe épaisse et argentée.'),
('Maine coon', 2, 'Chat de grande taille, à poils mi-longs.'),
('Singapura', 2, 'Chat de petite taille aux grands yeux en amandes.'),
('Sphynx', 2, 'Chat sans poils.');

-- ---------------------------------------------
-- AJOUT DE LA COLONNE race_id A LA TABLE Animal
-- ---------------------------------------------
ALTER TABLE Animal ADD COLUMN race_id SMALLINT UNSIGNED;

ALTER TABLE Animal
ADD CONSTRAINT fk_race_id FOREIGN KEY (race_id) REFERENCES Race(id);

-- -------------------------
-- REMPLISSAGE DE LA COLONNE
-- -------------------------
UPDATE Animal SET race_id = 1 WHERE id IN (1, 13, 20, 18, 22, 25, 26, 28);
UPDATE Animal SET race_id = 2 WHERE id IN (12, 14, 19, 7);
UPDATE Animal SET race_id = 3 WHERE id IN (17, 21, 27);
UPDATE Animal SET race_id = 4 WHERE id IN (33, 35, 37, 41, 44, 31, 3);
UPDATE Animal SET race_id = 5 WHERE id IN (43, 40, 30, 32, 42, 34, 39, 8);
UPDATE Animal SET race_id = 6 WHERE id IN (29, 36, 38);

-- -------------------------------------------------------
-- AJOUT DES COLONNES mere_id ET pere_id A LA TABLE Animal
-- -------------------------------------------------------
ALTER TABLE Animal ADD COLUMN mere_id SMALLINT UNSIGNED;

ALTER TABLE Animal
ADD CONSTRAINT fk_mere_id FOREIGN KEY (mere_id) REFERENCES Animal(id);

ALTER TABLE Animal ADD COLUMN pere_id SMALLINT UNSIGNED;

ALTER TABLE Animal
ADD CONSTRAINT fk_pere_id FOREIGN KEY (pere_id) REFERENCES Animal(id);

-- -------------------------------------------
-- REMPLISSAGE DES COLONNES mere_id ET pere_id
-- -------------------------------------------
UPDATE Animal SET mere_id = 18, pere_id = 22 WHERE id = 1;
UPDATE Animal SET mere_id = 7, pere_id = 21 WHERE id = 10;
UPDATE Animal SET mere_id = 41, pere_id = 31 WHERE id = 3;
UPDATE Animal SET mere_id = 40, pere_id = 30 WHERE id = 2;