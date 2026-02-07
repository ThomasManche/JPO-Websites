DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_user WHERE usename = 'program') THEN
      CREATE USER program WITH PASSWORD 'program';
   END IF;
END
$$;

GRANT ALL PRIVILEGES ON DATABASE "JPO" TO program;

CREATE TABLE insa_user (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(30) UNIQUE NOT NULL,
    mdp VARCHAR(70) NOT NULL
);

CREATE TABLE insa_safe_user (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(30) UNIQUE NOT NULL,
    hash_mdp VARCHAR(70) NOT NULL
);

INSERT INTO "insa_user" (username, mdp)
VALUES ('INSACyber', 'INSACyber');

INSERT INTO "insa_safe_user" (username, hash_mdp)
VALUES ('INSACyber','f52f643fe7549b35bc5e2fc983244db77ab3295616fc9712cdf8e360eaed3719');
