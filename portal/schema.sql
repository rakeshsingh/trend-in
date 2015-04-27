drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  date text not null,
  url text not null,
  type text,
  title text,
  description text, 
  rank  integer
);