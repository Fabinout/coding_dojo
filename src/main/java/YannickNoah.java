import java.util.List;

public class YannickNoah {

    private static String[] scores= new String[4];

    static {

        scores[0]="0";
        scores[1]="15";
        scores[2]="30";
        scores[3]="40";

    }
    private static final String SEP = "-";

    public static String compute(List<Boolean> points) {

        int leftPlayerScore = (int)points.stream().filter(aBoolean -> aBoolean).count();
        int rightPlayerScore = (int)points.stream().filter(aBoolean -> !aBoolean).count();
        if(leftPlayerScore == rightPlayerScore && leftPlayerScore != 0)
            return scores[leftPlayerScore] + "A";
        return scores[leftPlayerScore] + SEP + scores[rightPlayerScore];
    }
}
