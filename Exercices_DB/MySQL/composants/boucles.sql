-- WHILE / Stop qd faux
DELIMITER |
CREATE PROCEDURE compter_jusque_while(IN p_nombre INT)
BEGIN
    DECLARE v_i INT DEFAULT 1;

    mega_while : WHILE v_i <= p_nombre DO       -- label mega_while créé pour boucle WHILE
        SELECT v_i as nombre;
        SET v_i = v_i + 1;
    END WHILE;
END |
DELIMITER ;

-- Appel while
CALL compter_jusque_while(5);


----------------------------
-- REPEAT / Stop qd vrai
DELIMITER |
CREATE PROCEDURE compter_jusque_repeat(IN p_nombre INT)
BEGIN  
    DECLARE v_i INT DEFAULT 1;

    super_repeat : REPEAT           -- label super_repeat créé pour boucle REPEAT
        SELECT v_i as nbre;
        SET v_i = v_i + 1;
    UNTIL v_i > p_nombre
    END REPEAT;
END |
DELIMITER ;

-- Appel Repeat
CALL compter_jusque_repeat(3);


---------------------------
-- LOOP / Boucle infinie. LABEL nécessaire pr stop avec LEAVE ds une boucle IF/END IF 
-- LEAVE / Stop boucle ou bloc
DELIMITER |
CREATE PROCEDURE compter_jusque_loop(IN p_nombre INT)
gde_procedure : BEGIN               -- label gde_procedure pour interruption avec LEAVE
    DECLARE v_i INT DEFAULT 1;

    giga_loop : LOOP                -- label giga_loop pour interruption avec LEAVE
        SELECT v_i as nombre;
        SET v_i = v_i + 1;
        IF v_i > p_nombre THEN
            SELECT 'Sortie de boucle' as issue;
            LEAVE giga_loop;
        ELSEIF v_i = 10 THEN
            SELECT 'Sortie de la procedure' as issue;
            LEAVE gde_procedure;
        END IF;
    END LOOP;
END|
DELIMITER ;

-- Appel LOOP / LEAVE
CALL compter_jusque_loop(4);
CALL compter_jusque_loop(12);


-----------------------------------
-- ITERATE / Utilisé dans une boucle. Lance nvelle itération de la boucle en ignorant instr° après ITERATE
DELIMITER |
CREATE PROCEDURE test_iterate()
BEGIN
    DECLARE v_i INT DEFAULT 0;
    boucle_while : WHILE v_i < 3 DO
        SET v_i = v_i + 1;

        SELECT v_i, 'avant if' as msg;
        IF v_i = 2 THEN
            ITERATE boucle_while;
        END IF;
        SELECT v_i, 'après if' as msg;
    END WHILE;
END |
DELIMITER ;

-- Appel ITERATE
CALL test_iterate();
