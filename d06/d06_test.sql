CREATE TABLE orbitmap
(
  cog text
  , orbiter text
);

delete from orbitmap;

INSERT INTO orbitmap (cog, orbiter) VALUES ( 'COM','B' );
INSERT INTO orbitmap (cog, orbiter) VALUES ( 'B','C' );
INSERT INTO orbitmap (cog, orbiter) VALUES ( 'C','D' );
INSERT INTO orbitmap (cog, orbiter) VALUES ( 'D','E' );
INSERT INTO orbitmap (cog, orbiter) VALUES ( 'E','F' );
INSERT INTO orbitmap (cog, orbiter) VALUES ( 'B','G' );
INSERT INTO orbitmap (cog, orbiter) VALUES ( 'G','H' );
INSERT INTO orbitmap (cog, orbiter) VALUES ( 'D','I' );
INSERT INTO orbitmap (cog, orbiter) VALUES ( 'E','J' );
INSERT INTO orbitmap (cog, orbiter) VALUES ( 'J','K' );
INSERT INTO orbitmap (cog, orbiter) VALUES ( 'K','L' );



WITH RECURSIVE orbiters as (
SELECT
  orbiter, cog
FROM orbitmap
UNION ALL
  SELECT
	  om.orbiter, om.cog
FROM orbitmap om inner join orbiters o ON om.orbiter = o.cog
) SELECT
  	count(1)
FROM
  orbiters