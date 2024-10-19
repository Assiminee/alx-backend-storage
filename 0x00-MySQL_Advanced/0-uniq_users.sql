-- creates a table users with some criteria
CREATE TABLE IF NOT EXISTS users
(
    id    INT          NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name  VARCHAR(255),
    PRIMARY KEY (id)
)
