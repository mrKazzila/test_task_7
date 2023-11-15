email_examples = (
    # data, expected_result
    ('example@example.com', True),
    ('2exa_mple2@example.com', True),
    ('12345@12345.com', True),
    # invalid
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
    # invalid
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
    # invalid
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

get_data_field_type_example = (
    # data_field_value, expected_result
    ('2023-01-01', 'date'),
    ('01.01.2023', 'date'),
    ('+7 123 456 90 12', 'phone'),
    ('example@example.com', 'email'),
    ('example', 'text'),
    # invalid
    ('+7 23 3456 90 12', 'text'),
    ('01-01-2023', 'text'),
    ('2023.01.01', 'text'),
    ('exampleexample.com', 'text'),
)

set_types_for_field_example = (
    # data, expected_result
    (
        {'field1': 'value1'},
        {'field1': 'text'},
    ),
    (
        {'date1': '01.01.2023', 'date2': '2023-01-01', 'date3': '01-01-2023', 'date4': '2023.01.01'},
        {'date1': 'date', 'date2': 'date', 'date3': 'text', 'date4': 'text'},
    ),
    (
        {'phone1': '+7 123 456 90 12', 'phone2': '+7 23 3456 90 12'},
        {'phone1': 'phone', 'phone2': 'text'},
    ),
    (
        {'email1': 'example@example.com', 'email2': 'exampleexample.com'},
        {'email1': 'email', 'email2': 'text'},
    ),

)
