import org.junit.jupiter.api.Test;

import static java.util.Arrays.asList;
import static org.assertj.core.api.AssertionsForClassTypes.assertThat;
import static org.junit.jupiter.api.Assertions.*;

class YannickNoahTest {

    @Test
    void compute_left_player_scores_15_0() {
        compareScoresAndResult(true, "15-0");
    }

    private void compareScoresAndResult(boolean b, String s) {
        var result = YannickNoah.compute(asList(b));
        assertThat(result).isEqualTo(s);
    }

    @Test
    void compute_left_player_scores_twice_30_0() {
        var result = YannickNoah.compute(asList(true, true));
        assertThat(result).isEqualTo("30-0");
    }

    @Test
    void compute_left_player_scores_three_times_40_0(){
        var result=YannickNoah.compute(asList(true,true,true));
        assertThat(result).isEqualTo("40-0");
    }

    @Test
    void compute_left_player_scores_start_match(){
        var result=YannickNoah.compute(asList());
        assertThat(result).isEqualTo("0-0");
    }
    @Test
    void compute_right_player_scores_15_0(){
        var result=YannickNoah.compute(asList(false));
        assertThat(result).isEqualTo("0-15");
    }
    @Test
    void compute_right_player_scores_30_0(){

        var result=YannickNoah.compute(asList(false, false));
        assertThat(result).isEqualTo("0-30");
    }
    @Test
    void compute_both_players_scores_15A(){
        var result=YannickNoah.compute(asList(true, false));
        assertThat(result).isEqualTo("15A");
    }
    @Test
    void compute_both_players_scores_15_30(){
        var result=YannickNoah.compute(asList(true, false, false));
        assertThat(result).isEqualTo("15-30");
    }
}