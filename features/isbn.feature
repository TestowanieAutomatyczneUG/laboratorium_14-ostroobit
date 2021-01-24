Feature: ISBN-13 number checker
    Function that checks if given number is a valid ISBN-13 number

    Scenario Outline: Check if value is valid
        Given value equal to <value>
        When using check_valid function
        Then check_valid result should be <result>

        Examples:
            | value                  | result |
            | 123456                 |  False |
            | hahahaha               |  False |
            | hah-a-ha-hahaha-h      |  False |
            | 978-3-16-148410-0      |  True  |
            | 978-1-56619-909-4      |  True  |
            | 948-3-29-145410-0      |  False |
            # | 123456                 |  False |
            # | 123456                 |  False |
            # | 123456                 |  False |
            # | 123456                 |  False |
            # | 123456                 |  False |
            # | 123456                 |  False |
            # | 123456                 |  False |