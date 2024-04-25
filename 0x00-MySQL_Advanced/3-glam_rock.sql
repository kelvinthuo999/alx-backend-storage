--script to list all bands
SELECT band_name,
       IFNULL(SPLIT_STR(lifespan, '-', 1), 2022) - IFNULL(SPLIT_STR(lifespan, '-', -1), 2022) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
