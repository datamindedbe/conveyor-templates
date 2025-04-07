MODEL (
    name sqlmesh_example.seed2_model,
    kind SEED (
        path '../seeds/seed_data_2.csv'
    ),
    columns (
        id INTEGER,
        price DECIMAL(5, 2),
        category VARCHAR(50),
    )
);