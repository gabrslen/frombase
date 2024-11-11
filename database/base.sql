
CREATE SCHEMA `api_schema`;

CREATE TABLE `api_schema`.`names` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `idnames_UNIQUE` (`id` ASC) VISIBLE);

CREATE TABLE api_schema.passwords (
  id INT NOT NULL AUTO_INCREMENT,
  password VARCHAR(45) NULL,
  id_names INT NOT NULL,
  data_criacao DATETIME NULL,
  inativo TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (id),
  INDEX id_names_passwords_idx (id_names ASC) VISIBLE,
  CONSTRAINT id_names_passwords
    FOREIGN KEY (id_names)
    REFERENCES api_schema.names (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);