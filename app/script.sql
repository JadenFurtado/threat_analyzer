CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    email_id VARCHAR(50)
);

INSERT INTO users(username,email_id) VALUES("jadenFurtado","furtadojaden@gmail.com");
INSERT INTO users(username,email_id) VALUES("Jaden","jaden@gmail.com");

CREATE TABLE house(
    id INT AUTO_INCREMENT PRIMARY KEY,
    house_name VARCHAR(255),
    house_type VARCHAR(20),
    house_state VARCHAR(100),
    house_city VARCHAR(20),
    house_address VARCHAR(255),
    house_pin_code VARCHAR(6),
    users_id INT(10)
);

INSERT INTO house(
    house_name,
    house_type,
    house_state,
    house_city,
    house_address,
    house_pin_code,
    users_id
)VALUES(
    "B9 Golden Orchar 1",
    "Flat",
    "Maharashtra",
    "Mumbai",
    "Santacruz, Kalina, Sundernagar",
    "400098",
    1
);

CREATE TABLE house_images(
    img_id INT AUTO_INCREMENT PRIMARY KEY,
    image_url VARCHAR(50),
    image_description VARCHAR(20),
    house_id INT(10),
    CONSTRAINT (house_img) FOREIGN KEY (house_id) REFERENCES (id) FROM houses
);

CREATE TABLE rented_house(
    id INT AUTO_INCREMENT PRIMARY KEY,
    house_id INT(10),
    start_dates DATE,
    end_date DATE
);
ALTER TABLE rented_house ADD users_id INT(10);