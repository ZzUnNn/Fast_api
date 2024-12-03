-- upgrade --
CREATE TABLE IF NOT EXISTS `group` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `group_member` VARCHAR(255) NOT NULL,
    `group_id` INT NOT NULL  COMMENT '组号'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `student_name` VARCHAR(32) NOT NULL  COMMENT '学生名字',
    `student_ID` INT NOT NULL  COMMENT '学号',
    `group_id` INT NOT NULL,
    CONSTRAINT `fk_student_group_81bcd2a3` FOREIGN KEY (`group_id`) REFERENCES `group` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
