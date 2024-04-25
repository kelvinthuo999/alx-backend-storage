--script that calculates and stores average score
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_projects INT;
    DECLARE average_score FLOAT;

    -- Compute total score for the user
    SELECT SUM(score) INTO total_score
    FROM corrections
    WHERE user_id = user_id;

    -- Compute total number of projects for the user
    SELECT COUNT(DISTINCT project_id) INTO total_projects
    FROM corrections
    WHERE user_id = user_id;

    -- Compute average score
    IF total_projects > 0 THEN
        SET average_score = total_score / total_projects;
    ELSE
        SET average_score = 0;
    END IF;

    -- Update user's average score
    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;
END //

DELIMITER ;
