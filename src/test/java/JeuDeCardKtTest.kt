import model.Card
import model.Rank
import model.Suit
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

internal class JeuDeCardKtTest {

    @Test
    fun testGetScore() {

        val deck = createDefaultDeck()
        assertEquals(52, deck.size())

    }

    @Test
    fun testShuffle() {
        val deck = createDefaultDeck()
        val firstCards = mutableSetOf<Int>()
        for (i in 1..10){
            firstCards.add(deck.peek().hashCode())
            deck.shuffle()
        }
        assertEquals(10@, firstCards.size)
    }

    @Test
    fun `test Pick A Card`() {
        val deck = createDefaultDeck()
        val initialSize = deck.size()

        val card = deck.pick()

        assertEquals(initialSize - 1, deck.size())
        assertEquals(card, Card(Suit.HEART, Rank.ACE))
    }
}


