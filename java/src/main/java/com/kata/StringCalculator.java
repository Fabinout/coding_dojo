package com.kata;

public class StringCalculator {


    public int add(String s) throws FormatException {
        int result = 0;
        String[] numbers = s.split("[,\n]");
        for (String number : numbers) {
            if(number.isEmpty()) throw new FormatException();
            result += Integer.parseInt(number);
        }
        return result;
    }

}
