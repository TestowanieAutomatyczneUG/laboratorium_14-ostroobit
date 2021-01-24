Feature: Hamming
    Hamming is counting different letters in strands

    Scenario Outline: Two strands given
        Given two strands
        When <strand1> and <strand2> are same length
        Then result should be <result>
        
        Examples:
            |       strand1 |       strand2 | result |
            | GGACTGAAATCTG | GGACTGAAATCTG |      0 |
            | GGBCTGAAATCTG | GGACTGAAATCTG |      1 |
            | GGACTGAAAETRG | GGACTGAAATCTG |      3 |
            | GABAGREAATCTG | GGACTGAAATCTG |      6 |
