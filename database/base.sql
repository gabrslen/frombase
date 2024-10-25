
CREATE SCHEMA `api_schema`;

CREATE TABLE `api_schema`.`names_table` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `idnames_table_UNIQUE` (`id` ASC) VISIBLE);
