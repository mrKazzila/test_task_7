email_examples = (
    # data, expected_result
    ('example@example.com', True),
    ('2exa_mple2@example.com', True),
    ('12345@12345.com', True),
    ('example@examplecom', False),
    ('exampleexample.com', False),
    ('@example.com', False),
    ('example', False),
    ('', False),
)

date_examples = (
    # data, expected_result
    ('01.01.2023', True),
    ('2023-01-01', True),
    ('2023-01.01',  False),
    ('2023.01.01', False),
    ('01-01-2023', False),
    ('01.2023.01', False),
    ('01-2023-01', False),
    ('1.1.1', False),
    ('', False),
    (' ', False),
    (' ', False),
)

phone_example = (
    # data, expected_result
    ('+7 123 456 90 12', True),
    ('+7 123 4567 890 12', False),
    ('+7 1239 67 820 2', False),
    ('+7323456789012', False),
    ('+7 223 4567 890 12 1', False),
    ('7 123 4567 890 12', False),
    ('8 123 4567 890 12', False),
    ('123 4567 890 12', False),
    ('+7 123', False),
    ('', False),
    (' ', False),
    ('+', False),
)
