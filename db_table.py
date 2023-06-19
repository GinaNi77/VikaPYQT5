script = """
DROP SCHEMA IF EXISTS `window_comp` ;

CREATE SCHEMA IF NOT EXISTS `window_comp` DEFAULT CHARACTER SET utf8 ;
USE `window_comp` ;

DROP TABLE IF EXISTS `window_comp`.`Customer` ;

CREATE TABLE IF NOT EXISTS `window_comp`.`Customer` (
  `idCustomer` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `surname` VARCHAR(45) NULL,
  `phone` VARCHAR(11) NULL,
  PRIMARY KEY (`idCustomer`));

DROP TABLE IF EXISTS `window_comp`.`OrderCard` ;

CREATE TABLE IF NOT EXISTS `window_comp`.`OrderCard` (
  `idOrderCard` INT NOT NULL AUTO_INCREMENT,
  `costOrderCard` DECIMAL(10,2) NULL,
  `idCustomer` INT NOT NULL,
  PRIMARY KEY (`idOrderCard`),
  CONSTRAINT `idCustomerOC`
    FOREIGN KEY (`idCustomer`)
    REFERENCES `window_comp`.`Customer` (`idCustomer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

DROP TABLE IF EXISTS `window_comp`.`Product` ;

CREATE TABLE IF NOT EXISTS `window_comp`.`Product` (
  `idProduct` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(425) NULL,
  `material` VARCHAR(45) NULL,
  `size` VARCHAR(45) NULL,
  `costProduct` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`idProduct`));

DROP TABLE IF EXISTS `window_comp`.`Order` ;

CREATE TABLE IF NOT EXISTS `window_comp`.`Order` (
  `idOrder` INT NOT NULL AUTO_INCREMENT,
  `idOrderCard` INT NOT NULL,
  `idProduct` INT NOT NULL,
  `amount` INT NOT NULL,
  `costOrder` DECIMAL(10,2) NULL,
  PRIMARY KEY (`idOrder`),
  CONSTRAINT `idOrderCard`
    FOREIGN KEY (`idOrderCard`)
    REFERENCES `window_comp`.`OrderCard` (`idOrderCard`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idProduct`
    FOREIGN KEY (`idProduct`)
    REFERENCES `window_comp`.`Product` (`idProduct`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


DROP TABLE IF EXISTS `window_comp`.`InstallationWork` ;

CREATE TABLE IF NOT EXISTS `window_comp`.`InstallationWork` (
  `idInstallationWork` INT NOT NULL AUTO_INCREMENT,
  `beginDate` DATE NOT NULL,
  `endDate` DATE NOT NULL,
  `costWork` DECIMAL(10,2) NULL,
  `idOrderCard` INT NOT NULL,
  PRIMARY KEY (`idInstallationWork`),
  CONSTRAINT `idOrderCardW`
    FOREIGN KEY (`idOrderCard`)
    REFERENCES `window_comp`.`OrderCard` (`idOrderCard`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


DROP TABLE IF EXISTS `window_comp`.`Payment` ;

CREATE TABLE IF NOT EXISTS `window_comp`.`Payment` (
  `idPayment` INT NOT NULL AUTO_INCREMENT,
  `paymentDate` DATE NOT NULL,
  `costPayment` DECIMAL(10,2) NULL,
  `idOrderCard` INT NOT NULL,
  PRIMARY KEY (`idPayment`),
  CONSTRAINT `idOrderCardP`
    FOREIGN KEY (`idOrderCard`)
    REFERENCES `window_comp`.`OrderCard` (`idOrderCard`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
"""