-- -----------------------------------------------------
-- Table `employees`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT NOT NULL PRIMARY KEY,
    username VARCHAR(45),
    password VARCHAR(255),
    full_name VARCHAR(100),
    wage INT,
    start_date DATE,
    supervisor_username VARCHAR(45)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `shifts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS shifts (
    shift_id INT NOT NULL PRIMARY KEY,
    shift_date DATE,
    duration VARCHAR(10)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `employee_shifts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS employee_shifts (
    employee_id INT NOT NULL,
    shift_id INT NOT NULL,
    PRIMARY KEY (employee_id, shift_id),
    CONSTRAINT fk_employee_shift_employee_id FOREIGN KEY (employee_id)
        REFERENCES employees (employee_id)
        ON DELETE NO ACTION ON UPDATE NO ACTION,
    CONSTRAINT fk_employee_shift_shift_id FOREIGN KEY (shift_id)
        REFERENCES shifts (shift_id)
        ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT NOT NULL PRIMARY KEY,
    username VARCHAR(45),
    password VARCHAR(255),
    birthday DATE,
    reward_points INT,
    full_name VARCHAR(100)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`customer_orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`customer_orders` (
  `order_id` INT NOT NULL,
  `status` VARCHAR(45) NULL,
  `total_price` DECIMAL(10,2) NULL,
  `employee_id` INT NULL,
  `customer_id` INT NULL,
  PRIMARY KEY (`order_id`),
  INDEX `employee_id_idx` (`employee_id` ASC) VISIBLE,
  INDEX `customer_id_idx` (`customer_id` ASC) VISIBLE,
  CONSTRAINT `fk_order_employee`
    FOREIGN KEY (`employee_id`)
    REFERENCES `mydb`.`employees` (`employee_id`)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
  CONSTRAINT `fk_order_customer`
    FOREIGN KEY (`customer_id`)
    REFERENCES `mydb`.`customers` (`customer_id`)
    ON DELETE SET NULL
    ON UPDATE CASCADE
)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dishes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS dishes (
    dish_id INT NOT NULL PRIMARY KEY,
    price DECIMAL(5,2),
    name VARCHAR(100)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `ingredients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS ingredients (
    ingredient_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(100),
    shelf_life DATE
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `suppliers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INT NOT NULL PRIMARY KEY,
    username VARCHAR(45),
    password VARCHAR(255),
    company_name VARCHAR(100)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `ingredient_orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS ingredient_orders (
    ingredient_order_id INT NOT NULL PRIMARY KEY,
    delivery_date DATE,
    date_ordered DATE,
    weight INT,
    quantity INT,
    employee_id INT,
    supplier_id INT,
    CONSTRAINT fk_ingredient_order_employee FOREIGN KEY (employee_id)
        REFERENCES employees (employee_id)
        ON DELETE NO ACTION ON UPDATE NO ACTION,
    CONSTRAINT fk_ingredient_order_supplier FOREIGN KEY (supplier_id)
        REFERENCES suppliers (supplier_id)
        ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `order_dishes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS order_dishes (
    order_id INT NOT NULL,
    dish_id INT NOT NULL,
    PRIMARY KEY (order_id, dish_id),
    CONSTRAINT fk_order_dish_order FOREIGN KEY (order_id)
        REFERENCES orders (order_id)
        ON DELETE NO ACTION ON UPDATE NO ACTION,
    CONSTRAINT fk_order_dish_dish FOREIGN KEY (dish_id)
        REFERENCES dishes (dish_id)
        ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `ingredient_order_items`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS ingredient_order_items (
    ingredient_id INT NOT NULL,
    ingredient_order_id INT NOT NULL,
    PRIMARY KEY (ingredient_id, ingredient_order_id),
    CONSTRAINT fk_ing_order_item_ingredient FOREIGN KEY (ingredient_id)
        REFERENCES ingredients (ingredient_id)
        ON DELETE NO ACTION ON UPDATE NO ACTION,
    CONSTRAINT fk_ing_order_item_order FOREIGN KEY (ingredient_order_id)
        REFERENCES ingredient_orders (ingredient_order_id)
        ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `dish_ingredients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS dish_ingredients (
    dish_id INT NOT NULL,
    ingredient_id INT NOT NULL,
    PRIMARY KEY (dish_id, ingredient_id),
    CONSTRAINT fk_dish_ingredient_dish FOREIGN KEY (dish_id)
        REFERENCES dishes (dish_id)
        ON DELETE NO ACTION ON UPDATE NO ACTION,
    CONSTRAINT fk_dish_ingredient_ingredient FOREIGN KEY (ingredient_id)
        REFERENCES ingredients (ingredient_id)
        ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `supplier_orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS supplier_orders (
    ingredient_order_id INT NOT NULL,
    supplier_id INT NOT NULL,
    PRIMARY KEY (ingredient_order_id, supplier_id),
    CONSTRAINT fk_supplier_order_order FOREIGN KEY (ingredient_order_id)
        REFERENCES ingredient_orders (ingredient_order_id)
        ON DELETE NO ACTION ON UPDATE NO ACTION,
    CONSTRAINT fk_supplier_order_supplier FOREIGN KEY (supplier_id)
        REFERENCES suppliers (supplier_id)
        ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB;
