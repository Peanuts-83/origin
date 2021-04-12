SET NAMES utf8;

DROP VIEW IF EXISTS V_Animal_details;
DROP VIEW IF EXISTS V_Animal_espece;
DROP VIEW IF EXISTS V_Animal_stagiaire;
DROP VIEW IF EXISTS V_Chien;
DROP VIEW IF EXISTS V_Chien_race;
DROP VIEW IF EXISTS V_Client;
DROP VIEW IF EXISTS V_Espece_dollars;
DROP VIEW IF EXISTS V_Nombre_espece;
DROP VIEW IF EXISTS V_Revenus_annee_espece;

DROP TABLE IF EXISTS Erreur;
DROP TABLE IF EXISTS Animal_histo;
DROP TABLE IF EXISTS VM_Revenus_annee_espece;

DROP TABLE IF EXISTS Adoption;
DROP TABLE IF EXISTS Animal;
DROP TABLE IF EXISTS Race;
DROP TABLE IF EXISTS Espece;
DROP TABLE IF EXISTS Client;

CREATE TABLE Client (
  id smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  nom varchar(100) NOT NULL,
  prenom varchar(60) NOT NULL,
  adresse varchar(200) DEFAULT NULL,
  code_postal varchar(6) DEFAULT NULL,
  ville varchar(60) DEFAULT NULL,
  pays varchar(60) DEFAULT NULL,
  email varbinary(100) DEFAULT NULL,
  date_naissance date DEFAULT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY ind_uni_email (email)
) ENGINE=InnoDB AUTO_INCREMENT=17;

LOCK TABLES Client WRITE;
INSERT INTO Client VALUES (1,'Dupont','Jean','Rue du Centre, 5','45810','Houtsiplou','France','jean.dupont@email.com',NULL),(2,'Boudur','Marie','Place de la Gare, 2','35840','Troudumonde','France','marie.boudur@email.com',NULL),(3,'Trachon','Fleur','Rue haute, 54b','3250','Belville','Belgique','fleurtrachon@email.com',NULL),
(4,'Van Piperseel','Julien',NULL,NULL,NULL,NULL,'jeanvp@email.com',NULL),
(5,'Nouvel','Johan',NULL,NULL,NULL,'Suisse','johanetpirlouit@email.com',NULL),(6,'Germain','Frank',NULL,NULL,NULL,NULL,'francoisgermain@email.com',NULL),
(7,'Antoine','Maximilien','Rue Moineau, 123','4580','Trocoul','Belgique','max.antoine@email.com',NULL),(8,'Di Paolo','Hector',NULL,NULL,NULL,'Suisse','hectordipao@email.com',NULL),
(9,'Corduro','Anaelle',NULL,NULL,NULL,NULL,'ana.corduro@email.com',NULL),
(10,'Faluche','Eline','Avenue circulaire, 7','45870','Garduche','France','elinefaluche@email.com',NULL),(11,'Penni','Carine','Boulevard Haussman, 85','1514','Plasse','Suisse','cpenni@email.com',NULL),(12,'Broussaille','Virginie','Rue du Fleuve, 18','45810','Houtsiplou','France','vibrousaille@email.com',NULL),
(13,'Durant','Hannah','Rue des Pendus, 66','1514','Plasse','Suisse','hhdurant@email.com',NULL),
(14,'Delfour','Elodie','Rue de Flore, 1','3250','Belville','Belgique','e.delfour@email.com',NULL),(15,'Kestau','Joel',NULL,NULL,NULL,NULL,'joel.kestau@email.com',NULL);
UNLOCK TABLES;


CREATE TABLE Espece (
  id smallint(6) unsigned NOT NULL AUTO_INCREMENT,
  nom_courant varchar(40) NOT NULL,
  nom_latin varchar(40) NOT NULL,
  description text,
  prix decimal(7,2) unsigned DEFAULT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY nom_latin (nom_latin)
) ENGINE=InnoDB AUTO_INCREMENT=8;

LOCK TABLES Espece WRITE;
INSERT INTO Espece VALUES (1,'Chien','Canis canis','Bestiole à quatre pattes qui aime les caresses et tire souvent la langue',200.00),(2,'Chat','Felis silvestris','Bestiole à quatre pattes qui saute très haut et grimpe aux arbres',150.00),
(3,'Tortue d''Hermann','Testudo hermanni','Bestiole avec une carapace très dure',140.00),
(4,'Perroquet amazone','Alipiopsitta xanthops','Joli oiseau parleur vert et jaune',700.00),(5,'Rat brun','Rattus norvegicus','Petite bestiole avec de longues moustaches et une longue queue sans poils',10.00),(6,'Perruche terrestre','Pezoporus wallicus','Joli oiseau aux plumes majoritairement vert brillant',20.00);
UNLOCK TABLES;


CREATE TABLE Race (
  id smallint(6) unsigned NOT NULL AUTO_INCREMENT,
  nom varchar(40) NOT NULL,
  espece_id smallint(6) unsigned NOT NULL,
  description text,
  prix decimal(7,2) unsigned DEFAULT NULL,
  date_insertion datetime DEFAULT NULL,
  utilisateur_insertion varchar(20) DEFAULT NULL,
  date_modification datetime DEFAULT NULL,
  utilisateur_modification varchar(20) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=11;

LOCK TABLES Race WRITE;
INSERT INTO Race VALUES (1,'Berger allemand',1,'Chien sportif et élégant au pelage dense, noir-marron-fauve, noir ou gris.',485.00,'2012-05-21 00:53:36','Test','2012-05-21 00:53:36','Test'),(2,'Berger blanc suisse',1,'Petit chien au corps compact, avec des pattes courtes mais bien proportionnées et au pelage tricolore ou bicolore.',935.00,'2012-05-21 00:53:36','Test','2012-05-21 00:53:36','Test'),
(3,'Singapura',2,'Chat de petite taille aux grands yeux en amandes.',985.00,'2012-05-21 00:53:36','Test','2012-05-21 00:53:36','Test'),
(4,'Bleu russe',2,'Chat aux yeux verts et à la robe épaisse et argentée.',835.00,'2012-05-21 00:53:36','Test','2012-05-21 00:53:36','Test'),(5,'Maine Coon',2,'Chat de grande taille, à poils mi-longs.',735.00,'2012-05-21 00:53:36','Test','2012-05-27 18:10:46','student@localhost'),(7,'Sphynx',2,'Chat sans poils.',1235.00,'2012-05-21 00:53:36','Test','2012-05-21 00:53:36','Test'),
(8,'Nebelung',2,'Chat bleu russe, mais avec des poils longs...',985.00,'2012-05-21 00:53:36','Test','2012-05-21 00:53:36','Test'),
(9,'Rottweiller',1,'Chien d''apparence solide, bien musclé, à la robe noire avec des taches feu bien délimitées.',630.00,'2012-05-21 00:53:36','Test','2012-05-22 00:54:13','student@localhost'),(10,'Yorkshire terrier',1,'Chien de petite taille au pelage long et soyeux de couleur bleu et feu.',700.00,'2012-05-22 00:58:25','student@localhost','2012-05-22 00:58:25','student@localhost');
UNLOCK TABLES;


CREATE TABLE Animal (
  id smallint(6) unsigned NOT NULL AUTO_INCREMENT,
  sexe char(1) DEFAULT NULL,
  date_naissance datetime NOT NULL,
  nom varchar(30) DEFAULT NULL,
  commentaires text,
  espece_id smallint(6) unsigned NOT NULL,
  race_id smallint(6) unsigned DEFAULT NULL,
  mere_id smallint(6) unsigned DEFAULT NULL,
  pere_id smallint(6) unsigned DEFAULT NULL,
  disponible tinyint(1) DEFAULT '1',
  PRIMARY KEY (id),
  UNIQUE KEY ind_uni_nom_espece_id (nom,espece_id)
) ENGINE=InnoDB AUTO_INCREMENT=81;

LOCK TABLES Animal WRITE;
INSERT INTO Animal VALUES (1,'M','2010-04-05 13:43:00','Rox','Mordille beaucoup',1,1,18,22,1),(2,NULL,'2010-03-24 02:23:00','Roucky',NULL,2,NULL,40,30,1),(3,'F','2010-09-13 15:02:00','Schtroumpfette',NULL,2,4,41,31,0),
(4,'F','2009-08-03 05:12:00',NULL,'Bestiole avec une carapace très dure',3,NULL,NULL,NULL,1),(5,NULL,'2010-10-03 16:44:00','Choupi','Né sans oreille gauche',2,NULL,NULL,NULL,0),(6,'F','2009-06-13 08:17:00','Bobosse','Carapace bizarre',3,NULL,NULL,NULL,1),
(7,'F','2008-12-06 05:18:00','Caroline',NULL,1,2,NULL,NULL,1),(8,'M','2008-09-11 15:38:00','Bagherra',NULL,2,5,NULL,NULL,0),(9,NULL,'2010-08-23 05:18:00',NULL,'Bestiole avec une carapace très dure',3,NULL,NULL,NULL,1),
(10,'M','2010-07-21 15:41:00','Bobo','Petit pour son âge',1,NULL,7,21,1),(11,'F','2008-02-20 15:45:00','Canaille',NULL,1,NULL,NULL,NULL,1),(12,'F','2009-05-26 08:54:00','Cali',NULL,1,2,NULL,NULL,1),
(13,'F','2007-04-24 12:54:00','Rouquine',NULL,1,1,NULL,NULL,1),(14,'F','2009-05-26 08:56:00','Fila',NULL,1,2,NULL,NULL,1),(15,'F','2008-02-20 15:47:00','Anya',NULL,1,NULL,NULL,NULL,0),
(16,'F','2009-05-26 08:50:00','Louya',NULL,1,NULL,NULL,NULL,0),(17,'F','2008-03-10 13:45:00','Welva',NULL,1,NULL,NULL,NULL,1),(18,'F','2007-04-24 12:59:00','Zira',NULL,1,1,NULL,NULL,0),
(19,'F','2009-05-26 09:02:00','Java',NULL,2,4,NULL,NULL,1),(20,NULL,'2007-04-24 12:45:00','Balou',NULL,1,1,NULL,NULL,1),(21,'F','2008-03-10 13:43:00','Pataude','Rhume chronique',1,NULL,NULL,NULL,0),
(22,'M','2007-04-24 12:42:00','Bouli',NULL,1,1,NULL,NULL,1),(24,'M','2007-04-12 05:23:00','Cartouche',NULL,1,NULL,NULL,NULL,1),(25,'M','2006-05-14 15:50:00','Zambo',NULL,1,1,NULL,NULL,1),
(26,'M','2006-05-14 15:48:00','Samba',NULL,1,1,NULL,NULL,0),(27,'M','2008-03-10 13:40:00','Moka',NULL,1,NULL,NULL,NULL,0),(28,'M','2006-05-14 15:40:00','Pilou',NULL,1,1,NULL,NULL,1),
(29,'M','2009-05-14 06:30:00','Fiero',NULL,2,3,NULL,NULL,1),(30,'M','2007-03-12 12:05:00','Zonko',NULL,2,5,NULL,NULL,0),(31,'M','2008-02-20 15:45:00','Filou',NULL,2,4,NULL,NULL,1),
(32,'M','2009-07-26 11:52:00','Spoutnik',NULL,3,NULL,52,NULL,0),(33,'M','2006-05-19 16:17:00','Caribou',NULL,2,4,NULL,NULL,1),(34,'M','2008-04-20 03:22:00','Capou',NULL,2,5,NULL,NULL,1),
(35,'M','2006-05-19 16:56:00','Raccou','Pas de queue depuis la naissance',2,4,NULL,NULL,1),(36,'M','2009-05-14 06:42:00','Boucan',NULL,2,3,NULL,NULL,1),(37,'F','2006-05-19 16:06:00','Callune',NULL,2,8,NULL,NULL,1),
(38,'F','2009-05-14 06:45:00','Boule',NULL,2,3,NULL,NULL,0),(39,'F','2008-04-20 03:26:00','Zara',NULL,2,5,NULL,NULL,0),(40,'F','2007-03-12 12:00:00','Milla',NULL,2,5,NULL,NULL,0),
(41,'F','2006-05-19 15:59:00','Feta',NULL,2,4,NULL,NULL,0),(42,'F','2008-04-20 03:20:00','Bilba','Sourde de l''oreille droite à 80%',2,5,NULL,NULL,0),(43,'F','2007-03-12 11:54:00','Cracotte',NULL,2,5,NULL,NULL,1),
(44,'F','2006-05-19 16:16:00','Cawette',NULL,2,8,NULL,NULL,1),(45,'F','2007-04-01 18:17:00','Nikki','Bestiole avec une carapace très dure',3,NULL,NULL,NULL,1),(46,'F','2009-03-24 08:23:00','Tortilla','Bestiole avec une carapace très dure',3,NULL,NULL,NULL,1),
(48,'F','2006-03-15 14:56:00','Lulla','Bestiole avec une carapace très dure',3,NULL,NULL,NULL,1),(49,'F','2008-03-15 12:02:00','Dana','Bestiole avec une carapace très dure',3,NULL,NULL,NULL,0),(50,'F','2009-05-25 19:57:00','Cheli','Bestiole avec une carapace très dure',3,NULL,NULL,NULL,1),
(51,'F','2007-04-01 03:54:00','Chicaca','Bestiole avec une carapace très dure',3,NULL,NULL,NULL,1),(52,'F','2006-03-15 14:26:00','Redbul','Insomniaque',3,NULL,NULL,NULL,1),
(54,'M','2008-03-16 08:20:00','Bubulle','Bestiole avec une carapace très dure',3,NULL,NULL,NULL,1),
(55,'M','2008-03-15 18:45:00','Relou','Surpoids',3,NULL,NULL,NULL,0),(56,'M','2009-05-25 18:54:00','Bulbizard','Bestiole avec une carapace très dure',3,NULL,NULL,NULL,1),
(57,'M','2007-03-04 19:36:00','Safran','Coco veut un gâteau !',4,NULL,NULL,NULL,0),
(58,'M','2008-02-20 02:50:00','Gingko','Coco veut un gâteau !',4,NULL,NULL,NULL,0),(59,'M','2009-03-26 08:28:00','Bavard','Coco veut un gâteau !',4,NULL,NULL,NULL,0),
(60,'F','2009-03-26 07:55:00','Parlotte','Coco veut un gâteau !',4,NULL,NULL,NULL,1),(61,'M','2010-11-09 00:00:00','Yoda',NULL,2,5,NULL,NULL,1),(62,'M','2010-11-05 00:00:00','Pipo',NULL,1,9,NULL,NULL,0),
(69,'F','2012-02-13 15:45:00','Baba',NULL,5,NULL,NULL,NULL,0),(70,'M','2012-02-13 15:48:00','Bibo','Agressif',5,NULL,72,73,1),(72,'F','2008-02-01 02:25:00','Momy',NULL,5,NULL,NULL,NULL,1),
(73,'M','2007-03-11 12:45:00','Popi',NULL,5,NULL,NULL,NULL,1),(75,'F','2007-03-12 22:03:00','Mimi',NULL,5,NULL,NULL,NULL,0),(76,'M','2012-03-12 00:00:00','Rocco',NULL,1,9,NULL,NULL,1),
(77,'F','2011-09-21 15:14:00','Bambi',NULL,2,NULL,NULL,NULL,1),(78,'M','2012-02-28 03:05:00','Pumba','Prématuré, à surveiller',1,9,NULL,NULL,1),(79,'M','2011-05-24 23:51:00','Lion',NULL,2,5,NULL,NULL,1);
UNLOCK TABLES;


CREATE TABLE Adoption (
  client_id smallint(5) unsigned NOT NULL,
  animal_id smallint(5) unsigned NOT NULL,
  date_reservation date NOT NULL,
  date_adoption date DEFAULT NULL,
  prix decimal(7,2) unsigned NOT NULL,
  paye tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (client_id,animal_id),
  UNIQUE KEY ind_uni_animal_id (animal_id)
) ENGINE=InnoDB;

LOCK TABLES Adoption WRITE;
INSERT INTO Adoption VALUES (1,8,'2012-05-21',NULL,735.00,1),(1,39,'2008-08-17','2008-08-17',735.00,1),(1,40,'2008-08-17','2008-08-17',735.00,1),
(2,3,'2011-03-12','2011-03-12',835.00,1),(2,18,'2008-06-04','2008-06-04',485.00,1),(3,27,'2009-11-17','2009-11-17',200.00,1),
(4,26,'2007-02-21','2007-02-21',485.00,1),(4,41,'2007-02-21','2007-02-21',835.00,1),(5,21,'2009-03-08','2009-03-08',200.00,1),
(6,16,'2010-01-27','2010-01-27',200.00,1),(7,5,'2011-04-05','2011-04-05',150.00,1),(8,42,'2008-08-16','2008-08-16',735.00,1),
(9,38,'2007-02-11','2007-02-11',985.00,1),(9,55,'2011-02-13','2011-02-13',140.00,1),(9,59,'2012-05-22',NULL,700.00,0),
(10,49,'2010-08-17','2010-08-17',140.00,0),(11,32,'2008-08-17','2010-03-09',140.00,1),(11,62,'2011-03-01','2011-03-01',630.00,0),
(12,15,'2012-05-22',NULL,200.00,1),(12,69,'2007-09-20','2007-09-20',10.00,1),(12,75,'2012-05-21',NULL,10.00,0),
(13,57,'2012-01-10','2012-01-10',700.00,1),(14,58,'2012-02-25','2012-02-25',700.00,1),(15,30,'2008-08-17','2008-08-17',735.00,1);
UNLOCK TABLES;


CREATE TABLE VM_Revenus_annee_espece (
  annee int(4) NOT NULL DEFAULT '0',
  espece_id smallint(6) unsigned NOT NULL DEFAULT '0',
  somme decimal(29,2) DEFAULT NULL,
  nb bigint(21) NOT NULL DEFAULT '0',
  PRIMARY KEY (annee,espece_id),
  KEY somme (somme)
) ENGINE=InnoDB;

LOCK TABLES VM_Revenus_annee_espece WRITE;
INSERT INTO VM_Revenus_annee_espece VALUES (2007,1,485.00,1),(2007,2,1820.00,2),(2007,5,10.00,1),(2008,1,485.00,1),(2008,2,2940.00,4),
(2008,3,140.00,1),(2009,1,400.00,2),(2010,1,200.00,1),(2010,3,140.00,1),(2011,1,630.00,1),
(2011,2,985.00,2),(2011,3,140.00,1),(2012,1,200.00,1),(2012,2,735.00,1),(2012,4,2100.00,3),(2012,5,10.00,1);
UNLOCK TABLES;


CREATE TABLE Animal_histo (
  id smallint(6) unsigned NOT NULL,
  sexe char(1) DEFAULT NULL,
  date_naissance datetime NOT NULL,
  nom varchar(30) DEFAULT NULL,
  commentaires text,
  espece_id smallint(6) unsigned NOT NULL,
  race_id smallint(6) unsigned DEFAULT NULL,
  mere_id smallint(6) unsigned DEFAULT NULL,
  pere_id smallint(6) unsigned DEFAULT NULL,
  disponible tinyint(1) DEFAULT '1',
  date_histo datetime NOT NULL,
  utilisateur_histo varchar(20) NOT NULL,
  evenement_histo char(6) NOT NULL,
  PRIMARY KEY (id,date_histo)
) ENGINE=InnoDB;

LOCK TABLES Animal_histo WRITE;
INSERT INTO Animal_histo VALUES (10,'M','2010-07-21 15:41:00','Bobo',NULL,1,NULL,7,21,1,'2012-05-22 01:00:34','student@localhost','UPDATE'),(19,'F','2009-05-26 09:02:00','Java',NULL,1,2,NULL,NULL,1,'2012-05-27 18:14:29','student@localhost','UPDATE'),(21,'F','2008-03-10 13:43:00','Pataude',NULL,1,NULL,NULL,NULL,0,'2012-05-27 18:10:40','student@localhost','UPDATE'),
(47,'F','2009-03-26 01:24:00','Scroupy','Bestiole avec une carapace très dure',3,NULL,NULL,NULL,1,'2012-05-22 01:00:34','student@localhost','DELETE'),(77,'F','0000-00-00 00:00:00','Toxi',NULL,1,NULL,NULL,NULL,1,'2012-05-27 18:12:38','student@localhost','DELETE');
UNLOCK TABLES;


CREATE TABLE Erreur (
  id tinyint(3) unsigned NOT NULL AUTO_INCREMENT,
  erreur varchar(255) DEFAULT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY erreur (erreur)
) ENGINE=InnoDB AUTO_INCREMENT=8;

LOCK TABLES Erreur WRITE;
INSERT INTO Erreur VALUES (5,'Erreur : date_adoption doit être >= à date_reservation.'),(3,'Erreur : paye doit valoir TRUE (1) ou FALSE (0).'),(1,'Erreur : sexe doit valoir \"M\", \"F\" ou NULL.');
UNLOCK TABLES;


ALTER TABLE Race ADD CONSTRAINT fk_race_espece_id FOREIGN KEY (espece_id) REFERENCES Espece (id);
ALTER TABLE Animal ADD CONSTRAINT fk_espece_id FOREIGN KEY (espece_id) REFERENCES Espece (id);
ALTER TABLE Animal ADD CONSTRAINT fk_mere_id FOREIGN KEY (mere_id) REFERENCES Animal (id);
ALTER TABLE Animal ADD CONSTRAINT fk_pere_id FOREIGN KEY (pere_id) REFERENCES Animal (id);
ALTER TABLE Animal ADD CONSTRAINT fk_race_id FOREIGN KEY (race_id) REFERENCES Race (id);
ALTER TABLE Adoption ADD CONSTRAINT fk_adoption_animal_id FOREIGN KEY (animal_id) REFERENCES Animal (id);
ALTER TABLE Adoption ADD CONSTRAINT fk_client_id FOREIGN KEY (client_id) REFERENCES Client (id);
ALTER TABLE VM_Revenus_annee_espece ADD CONSTRAINT fk_vm_revenu_espece_id FOREIGN KEY (espece_id) REFERENCES Espece (id) ON DELETE CASCADE;


DELIMITER |

CREATE TRIGGER before_insert_adoption BEFORE INSERT
ON Adoption FOR EACH ROW
BEGIN
    IF NEW.paye != TRUE                                     
    AND NEW.paye != FALSE     
      THEN
        INSERT INTO Erreur (erreur) VALUES ('Erreur : paye doit valoir TRUE (1) ou FALSE (0).');

    ELSEIF NEW.date_adoption < NEW.date_reservation THEN    
        INSERT INTO Erreur (erreur) VALUES ('Erreur : date_adoption doit être >= à date_reservation.');
    END IF;
END |

CREATE TRIGGER after_insert_adoption AFTER INSERT
ON Adoption FOR EACH ROW
BEGIN
    UPDATE Animal
    SET disponible = FALSE
    WHERE id = NEW.animal_id;

    INSERT INTO VM_Revenus_annee_espece (espece_id, annee, somme, nb)
    SELECT espece_id, YEAR(NEW.date_reservation), NEW.prix, 1
    FROM Animal
    WHERE id = NEW.animal_id
    ON DUPLICATE KEY UPDATE somme = somme + NEW.prix, nb = nb + 1;
END |

CREATE TRIGGER before_update_adoption BEFORE UPDATE
ON Adoption FOR EACH ROW
BEGIN
    IF NEW.paye != TRUE                                     
    AND NEW.paye != FALSE     
      THEN
        INSERT INTO Erreur (erreur) VALUES ('Erreur : paye doit valoir TRUE (1) ou FALSE (0).');

    ELSEIF NEW.date_adoption < NEW.date_reservation THEN    
        INSERT INTO Erreur (erreur) VALUES ('Erreur : date_adoption doit être >= à date_reservation.');
    END IF;
END |

CREATE TRIGGER after_update_adoption AFTER UPDATE
ON Adoption FOR EACH ROW
BEGIN
    IF OLD.animal_id <> NEW.animal_id THEN
        UPDATE Animal
        SET disponible = TRUE
        WHERE id = OLD.animal_id;

        UPDATE Animal
        SET disponible = FALSE
        WHERE id = NEW.animal_id;
    END IF;

    INSERT INTO VM_Revenus_annee_espece (espece_id, annee, somme, nb)
    SELECT espece_id, YEAR(NEW.date_reservation), NEW.prix, 1
    FROM Animal
    WHERE id = NEW.animal_id
    ON DUPLICATE KEY UPDATE somme = somme + NEW.prix, nb = nb + 1;

    UPDATE VM_Revenus_annee_espece
    SET somme = somme - OLD.prix, nb = nb - 1
    WHERE annee = YEAR(OLD.date_reservation)
    AND espece_id = (SELECT espece_id FROM Animal WHERE id = OLD.animal_id);
 
    DELETE FROM VM_Revenus_annee_espece
    WHERE nb = 0;
END |

CREATE TRIGGER after_delete_adoption AFTER DELETE
ON Adoption FOR EACH ROW
BEGIN
    UPDATE Animal
    SET disponible = TRUE
    WHERE id = OLD.animal_id;

    UPDATE VM_Revenus_annee_espece
    SET somme = somme - OLD.prix, nb = nb - 1
    WHERE annee = YEAR(OLD.date_reservation)
    AND espece_id = (SELECT espece_id FROM Animal WHERE id = OLD.animal_id);
 
    DELETE FROM VM_Revenus_annee_espece
    WHERE nb = 0;
END |

CREATE TRIGGER before_insert_animal BEFORE INSERT
ON Animal FOR EACH ROW
BEGIN
    IF NEW.sexe IS NOT NULL   
    AND NEW.sexe != 'M'       
    AND NEW.sexe != 'F'
    AND NEW.sexe != 'A'
      THEN
        INSERT INTO Erreur (erreur) VALUES ('Erreur : sexe doit valoir "M", "F", "A" ou NULL.');
    END IF;
END |

CREATE TRIGGER before_update_animal BEFORE UPDATE
ON Animal FOR EACH ROW
BEGIN
    IF NEW.sexe IS NOT NULL   
    AND NEW.sexe != 'M'       
    AND NEW.sexe != 'F'    
    AND NEW.sexe != 'A'
      THEN
        SET NEW.sexe = NULL;
    END IF;
END |

CREATE TRIGGER after_update_animal AFTER UPDATE
ON Animal FOR EACH ROW
BEGIN
    INSERT INTO Animal_histo (
        id, sexe, date_naissance, nom, commentaires, espece_id, race_id, 
        mere_id, pere_id, disponible, date_histo, utilisateur_histo, evenement_histo)
    VALUES (
        OLD.id, OLD.sexe, OLD.date_naissance, OLD.nom, OLD.commentaires, OLD.espece_id, OLD.race_id,
        OLD.mere_id, OLD.pere_id, OLD.disponible, NOW(), CURRENT_USER(), 'UPDATE');
END |

CREATE TRIGGER after_delete_animal AFTER DELETE
ON Animal FOR EACH ROW
BEGIN
    INSERT INTO Animal_histo (
        id, sexe, date_naissance, nom, commentaires, espece_id, race_id, 
        mere_id,  pere_id, disponible, date_histo, utilisateur_histo, evenement_histo)
    VALUES (
        OLD.id, OLD.sexe, OLD.date_naissance, OLD.nom, OLD.commentaires, OLD.espece_id, OLD.race_id,
        OLD.mere_id, OLD.pere_id, OLD.disponible, NOW(), CURRENT_USER(), 'DELETE');
END |

CREATE TRIGGER before_delete_espece BEFORE DELETE
ON Espece FOR EACH ROW
BEGIN
    DELETE FROM Race
    WHERE espece_id = OLD.id;
END |

CREATE TRIGGER before_insert_race BEFORE INSERT
ON Race FOR EACH ROW
BEGIN
    SET NEW.date_insertion = NOW();
    SET NEW.utilisateur_insertion = CURRENT_USER();
    SET NEW.date_modification = NOW();
    SET NEW.utilisateur_modification = CURRENT_USER();
END |

CREATE TRIGGER before_update_race BEFORE UPDATE
ON Race FOR EACH ROW
BEGIN
    SET NEW.date_modification = NOW();
    SET NEW.utilisateur_modification = CURRENT_USER();
END |

CREATE TRIGGER before_delete_race BEFORE DELETE
ON Race FOR EACH ROW
BEGIN
    UPDATE Animal 
    SET race_id = NULL
    WHERE race_id = OLD.id;
END |

DELIMITER ;

CREATE VIEW V_Animal_details AS 
select Animal.id,Animal.sexe,Animal.date_naissance,Animal.nom,Animal.commentaires,Animal.espece_id,Animal.race_id,
    Animal.mere_id,Animal.pere_id,Animal.disponible,Espece.nom_courant AS espece_nom,Race.nom AS race_nom 
from Animal 
join Espece on Animal.espece_id = Espece.id 
left join Race on Animal.race_id = Race.id;

CREATE VIEW V_Animal_espece AS 
select Animal.id,Animal.sexe,Animal.date_naissance,Animal.nom,Animal.commentaires,Animal.espece_id,Animal.race_id,
    Animal.mere_id,Animal.pere_id,Animal.disponible,Espece.nom_courant AS espece_nom,Espece.nom_latin AS espece_nom_latin 
from Animal 
join Espece on Espece.id = Animal.espece_id;

CREATE VIEW V_Animal_stagiaire AS 
select Animal.id,Animal.nom,Animal.sexe,Animal.date_naissance,Animal.espece_id,Animal.race_id,Animal.mere_id,Animal.pere_id,Animal.disponible 
from Animal 
where Animal.espece_id = 2
WITH CASCADED CHECK OPTION;

CREATE VIEW V_Chien AS 
select Animal.id,Animal.sexe,Animal.date_naissance,Animal.nom,Animal.commentaires,Animal.espece_id,Animal.race_id,Animal.mere_id,Animal.pere_id,Animal.disponible 
from Animal 
where Animal.espece_id = 1;

CREATE VIEW V_Chien_race AS 
select V_Chien.id,V_Chien.sexe,V_Chien.date_naissance,V_Chien.nom,V_Chien.commentaires,V_Chien.espece_id,V_Chien.race_id,V_Chien.mere_id,V_Chien.pere_id,V_Chien.disponible 
from V_Chien 
where V_Chien.race_id is not null
WITH CASCADED CHECK OPTION;

CREATE VIEW V_Client AS 
select Client.id,Client.nom,Client.prenom,Client.adresse,Client.code_postal,Client.ville,Client.pays,Client.email 
from Client;

CREATE VIEW V_Espece_dollars AS 
select Espece.id,Espece.nom_courant,Espece.nom_latin,Espece.description,round((Espece.prix * 1.30813),2) AS prix_dollars 
from Espece;

CREATE VIEW V_Nombre_espece AS 
select Espece.id,count(Animal.id) AS nb 
from Espece 
left join Animal on Animal.espece_id = Espece.id 
group by Espece.id;

CREATE VIEW V_Revenus_annee_espece AS 
select year(Adoption.date_reservation) AS annee,Espece.id AS espece_id,sum(Adoption.prix) AS somme,count(Adoption.animal_id) AS nb 
from Adoption 
join Animal on Animal.id = Adoption.animal_id
join Espece on Animal.espece_id = Espece.id 
group by year(Adoption.date_reservation),Espece.id;