DROP TABLE IF EXISTS "user";
DROP TABLE IF EXISTS "role";
DROP TABLE IF EXISTS "roles_users";

CREATE TABLE "user" (
        id SERIAL PRIMARY KEY,
        email VARCHAR(255),
        password VARCHAR(255),
        active BOOLEAN,
        UNIQUE (email)
);
CREATE TABLE "role" (
        id INTEGER NOT NULL,
        name VARCHAR(80),
        description VARCHAR(255),
        PRIMARY KEY (id),
        UNIQUE (name)
);
CREATE TABLE "roles_users" (
        user_id INTEGER,
        role_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES "user" (id),
        FOREIGN KEY(role_id) REFERENCES "role" (id)
);

INSERT INTO "user" VALUES ( 0,
                            'admin@nti-contest.ru',
                            'c8efa10c4e11e89c74faffbf735020b7',
                            TRUE);
