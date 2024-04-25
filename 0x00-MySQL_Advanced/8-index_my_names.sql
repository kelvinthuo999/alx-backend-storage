--create an index on a table and the name
CREATE INDEX idx_name_first ON names (LEFT(name, 1));
