-- Créer VIEW / requete SELECT dans un nom_view (CREATE VIEW ... AS...)
CREATE VIEW V_Animal_details
AS SELECT Animal.id, Animal.sexe, Animal.date_naissance, Animal.nom, Animal.commentaires, Animal.espece_id, Animal.race_id, Animal.mere_id, Animal.pere_id, Animal.disponible, Espece.nom_courant as espece, Race.nom as nom_race
FROM Animal
JOIN Espece ON Animal.espece_id=Espece.id
LEFT JOIN Race ON Animal.race_id=Race.id;

-- Créer VIEW avec liste des cols / alt aux alias du SELECT
CREATE VIEW V_Animal_details (id, sexe, date_naissance, nom, commentaires, espece_id, race_id, mere_id, pere_id, disponible, espece, nom_race)
AS SELECT Animal.id, Animal.sexe, Animal.date_naissance, Animal.nom, Animal.commentaires, 
       Animal.espece_id, Animal.race_id, Animal.mere_id, Animal.pere_id, Animal.disponible,
       Espece.nom_courant, Race.nom
FROM Animal
INNER JOIN Espece ON Animal.espece_id = Espece.id
LEFT JOIN Race ON Animal.race_id = Race.id;

-- Appel VIEW
SELECT * FROM V_Animal_details ORDER BY id;

-- Vue cols VIEW
DESCRIBE v_Animal_details;

-- VIEW sur chiens
CREATE VIEW V_chiens (id, sexe, date_naissance, nom, commentaires, espece_id, race_id, mere_id, pere_id, disponible, espece, nom_race)
AS SELECT Animal.id, Animal.sexe, Animal.date_naissance, Animal.nom, Animal.commentaires, 
       Animal.espece_id, Animal.race_id, Animal.mere_id, Animal.pere_id, Animal.disponible,
       Espece.nom_courant, Race.nom
FROM Animal
INNER JOIN Espece ON Animal.espece_id = Espece.id
LEFT JOIN Race ON Animal.race_id = Race.id
WHERE Espece.nom_courant='chien';

-- VIEW nbre de chats ou de chiens
CREATE OR REPLACE VIEW V_nbr_esp
AS SELECT Race.nom, Race.espece_id AS espece, COUNT(Animal.id) AS nb, group_concat(Animal.nom) as noms
FROM Race
LEFT JOIN Animal ON Animal.race_id = Race.id
GROUP BY Race.id;
-- Appel nbre de chats classé par race et par nom de chat
SELECT * FROM V_nbr_esp WHERE espece=2;

-- VIEW chiens dont on connnait la race depuis V_chiens
CREATE OR REPLACE VIEW V_chiens_race
AS SELECT * FROM V_chiens 
WHERE race_id IS NOT NULL;
-- Appel V_chiens_race avec CONCAT(noms)
SELECT *, GROUP_CONCAT(nom) FROM V_chiens_race GROUP BY race_id;

-- VIEW avec prix especes en $
CREATE OR REPLACE VIEW V_esp_en_dollar
AS SELECT nom_courant, CONCAT_WS(' ',ROUND(prix * 1.168, 2),'$') as prix_dollar 
FROM Espece;
-- Appel V_esp_en_dollar
SELECT * FROM V_esp_en_dollar;

-- VIEW Berger allemand depuis V_chiens
 SELECT id,sexe, nom, commentaires disponible FROM V_chiens WHERE race_id=1;

 -- VIEW V_nbr_esp JOIN Espece pour avoir nom_courant espece
 SELECT nom as nom_race, nom_courant as nom_espece, nb, COALESCE(noms, '...Vide...') as 'noms animaux' FROM V_nbr_esp JOIN Espece ON V_nbr_esp.espece=Espece.id;

-- VIEW Revenus par espece
CREATE OR REPLACE VIEW V_Revenus_annee_esp
AS SELECT espece_id, SUM(Adoption.prix) as somme, COUNT(Animal.id) as nbr, YEAR(date_reservation) as year
FROM Adoption
JOIN Animal ON Adoption.animal_id=Animal.id
JOIN Espece ON Animal.espece_id=Espece.id
GROUP BY year, espece_id;
