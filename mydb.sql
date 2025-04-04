-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Employee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Employee` (
  `Employee_id` INT NOT NULL,
  `Username` VARCHAR(45) NULL,
  `Password` VARCHAR(45) NULL,
  `Full_name` VARCHAR(45) NULL,
  `Wage` INT NULL,
  `S_Date` DATE NULL,
  `Super_username` VARCHAR(45) NULL,
  PRIMARY KEY (`Employee_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Shift`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Shift` (
  `Shift_ID` INT NOT NULL,
  `Date` DATE NULL,
  `Duration` VARCHAR(10) NULL,
  PRIMARY KEY (`Shift_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Employee_Shift`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Employee_Shift` (
  `E_ID` INT NOT NULL,
  `S_ID` INT NOT NULL,
  PRIMARY KEY (`E_ID`, `S_ID`),
  INDEX `S_ID_idx` (`S_ID` ASC) VISIBLE,
  CONSTRAINT `E_ID`
    FOREIGN KEY (`E_ID`)
    REFERENCES `mydb`.`Employee` (`Employee_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `S_ID`
    FOREIGN KEY (`S_ID`)
    REFERENCES `mydb`.`Shift` (`Shift_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Customer` (
  `Customer_ID` INT NOT NULL,
  `Username` VARCHAR(45) NULL,
  `Password` VARCHAR(45) NULL,
  `Birthday` DATE NULL,
  `Reward_points` INT NULL,
  `Full_name` VARCHAR(45) NULL,
  PRIMARY KEY (`Customer_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Order` (
  `Order_ID` INT NOT NULL,
  `Status` VARCHAR(45) NULL,
  `Total_Price` DECIMAL(10,2) NULL,
  `Emp_ID` INT NULL,
  `Cust_Id` INT NULL,
  PRIMARY KEY (`Order_ID`),
  INDEX `Emp_ID_idx` (`Emp_ID` ASC) VISIBLE,
  INDEX `Cust_ID_idx` (`Cust_Id` ASC) VISIBLE,
  CONSTRAINT `Emp_ID`
    FOREIGN KEY (`Emp_ID`)
    REFERENCES `mydb`.`Employee` (`Employee_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Cust_ID`
    FOREIGN KEY (`Cust_Id`)
    REFERENCES `mydb`.`Customer` (`Customer_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Dish`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Dish` (
  `Dish_ID` INT NOT NULL,
  `Price` DECIMAL(5,2) NULL,
  `Name` VARCHAR(45) NULL,
  PRIMARY KEY (`Dish_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Ingredient`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Ingredient` (
  `Ing_ID` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Shelf_life` DATE NULL,
  PRIMARY KEY (`Ing_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Supplier`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Supplier` (
  `Supplier_ID` INT NOT NULL,
  `Username` VARCHAR(45) NULL,
  `Password` VARCHAR(45) NULL,
  `Company_name` VARCHAR(45) NULL,
  PRIMARY KEY (`Supplier_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Ingred_Order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Ingred_Order` (
  `Ingred_Order_ID` INT NOT NULL,
  `Deliver_date` DATE NULL,
  `Date_Ordered` DATE NULL,
  `Weight` INT NULL,
  `Quantity` INT NULL,
  `Emp_ID` INT NULL,
  `Supp_ID` INT NULL,
  PRIMARY KEY (`Ingred_Order_ID`),
  INDEX `Emp_ID_idx` (`Emp_ID` ASC) VISIBLE,
  INDEX `Supp_ID_idx` (`Supp_ID` ASC) VISIBLE,
  CONSTRAINT `Emp_ID`
    FOREIGN KEY (`Emp_ID`)
    REFERENCES `mydb`.`Employee` (`Employee_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Supp_ID`
    FOREIGN KEY (`Supp_ID`)
    REFERENCES `mydb`.`Supplier` (`Supplier_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Order_Dish`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Order_Dish` (
  `O_ID` INT NOT NULL,
  `D_ID` INT NOT NULL,
  PRIMARY KEY (`O_ID`, `D_ID`),
  INDEX `D_ID_idx` (`D_ID` ASC) VISIBLE,
  CONSTRAINT `O_ID`
    FOREIGN KEY (`O_ID`)
    REFERENCES `mydb`.`Order` (`Order_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `D_ID`
    FOREIGN KEY (`D_ID`)
    REFERENCES `mydb`.`Dish` (`Dish_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Ingredient_Ingred_Order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Ingredient_Ingred_Order` (
  `Ing_ID` INT NOT NULL,
  `Ingred_Ord_ID` INT NOT NULL,
  PRIMARY KEY (`Ing_ID`, `Ingred_Ord_ID`),
  INDEX `Ingred_Ord_ID_idx` (`Ingred_Ord_ID` ASC) VISIBLE,
  CONSTRAINT `Ing_ID`
    FOREIGN KEY (`Ing_ID`)
    REFERENCES `mydb`.`Ingredient` (`Ing_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Ingred_Ord_ID`
    FOREIGN KEY (`Ingred_Ord_ID`)
    REFERENCES `mydb`.`Ingred_Order` (`Ingred_Order_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Dish_Ingredient`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Dish_Ingredient` (
  `D_ID` INT NOT NULL,
  `I_ID` INT NOT NULL,
  PRIMARY KEY (`D_ID`, `I_ID`),
  INDEX `I_ID_idx` (`I_ID` ASC) VISIBLE,
  CONSTRAINT `D_ID`
    FOREIGN KEY (`D_ID`)
    REFERENCES `mydb`.`Dish` (`Dish_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `I_ID`
    FOREIGN KEY (`I_ID`)
    REFERENCES `mydb`.`Ingredient` (`Ing_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Supplier_Order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Supplier_Order` (
  `O_ID` INT NOT NULL,
  `S_ID` INT NOT NULL,
  PRIMARY KEY (`O_ID`, `S_ID`),
  INDEX `S_ID_idx` (`S_ID` ASC) VISIBLE,
  CONSTRAINT `FK_SupplierOrder_IngredOrder`
    FOREIGN KEY (`O_ID`)
    REFERENCES `mydb`.`Ingred_Order` (`Ingred_Order_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_SupplierOrder_Supplier`
    FOREIGN KEY (`S_ID`)
    REFERENCES `mydb`.`Supplier` (`Supplier_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
