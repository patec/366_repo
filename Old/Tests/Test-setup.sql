CREATE TABLE user (
    uid INT,
    name VARCHAR(100),
    PRIMARY KEY(uid)
);

CREATE TABLE account (
    uid INT,
    accountid INT,
    accountname VARCHAR(20),
    PRIMARY KEY (accountid),
    FOREIGN KEY(uid) references user(uid)
);


