-- TEMP TABLE / Création 1
-- Création à neuf
CREATE TEMPORARY TABLE Temp_test(
    id SMALLINT(3) UNSIGNED AUTO_INCREMENT NOT NULL,
    nom VARCHAR(7) NOT NULL,
    comments TEXT,
    PRIMARY KEY (id)
) Engine=InnoDB;
-- Remplissage données
INSERT INTO Temp_test (nom, comments)
SELECT nom, email FROM Client;

-- TEMP TABLE / Création 2
-- Copie table existante (vide)
CREATE TEMPORARY TABLE Erreur_bak 
LIKE Erreur;
-- Remplissage par copie des données
INSERT INTO Erreur_bak 
SELECT * FROM Erreur;

-- TEMP TABLE / Création 3
-- Depuis SELECT en direct / INDEX et AUTO_INCREMENT non conservés!
CREATE TEMPORARY TABLE Race_bak
SELECT * FROM Race;


-- TEMPORARY TABLE in PROCEDURE to store data from PROCEDURE
DELIMITER | 
CREATE PROCEDURE p_adoption_non_payee()
BEGIN
    DROP TEMPORARY TABLE IF EXISTS Adoptions_non_payees;
    CREATE TEMPORARY TABLE Adoptions_non_payees 
    SELECT Client.id AS client_id, Client.nom AS client_nom, Client.prenom AS client_prenom, Client.email AS client_email, Animal.nom AS animal_nom, Espece.nom_courant as espece, Race.nom AS race, Adoption.date_reservation, Adoption.date_adoption, Adoption.prix
    FROM Adoption
    JOIN Animal ON Adoption.animal_id=Animal.id
    JOIN Client ON Adoption.client_id=Client.id
    JOIN Espece ON Animal.espece_id=Espece.id
    LEFT JOIN Race ON ANimal.race_id=Race.id
    WHERE Adoption.paye IS FALSE;
END |
DELIMITER ;

-- Création de la table temporaire par appel de la procedure
CALL p_adoption_non_payee();

-- SELECT ds la table temp
SELECT client_nom AS nom, client_prenom AS prenom, client_email AS email, animal_nom AS animal, prix
FROM Adoptions_non_payees;


