package com.kata;


import static org.assertj.core.api.AssertionsForInterfaceTypes.assertThat;

import junitparams.FileParameters;
import junitparams.JUnitParamsRunner;
import org.junit.Test;
import org.junit.runner.RunWith;


@RunWith(JUnitParamsRunner.class)
public class StringCalculatorTest {

    @Test
    @FileParameters(value="src\\main\\resources\\input.csv")
    public void should_calculate(String input, int expectedResult) throws FormatException {
        StringCalculator stringCalculator = new StringCalculator();
        int result = stringCalculator.add(input);
        assertThat(result).isEqualTo(expectedResult);
    }

    @Test
    public void new_line_should_be_a_valid_separator() throws FormatException {
        should_calculate("1\n2", 3);
    }
}