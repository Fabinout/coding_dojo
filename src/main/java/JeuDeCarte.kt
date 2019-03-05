import model.Card
import model.Deck
import model.Rank
import model.Suit

fun createDefaultDeck(): Deck {
    val listOfCards: List<Card> =
            Suit.values().flatMap { suit ->
                Rank.values()
                        .map { rank ->
                            Card(suit, rank)
                        }
            }
    return Deck(listOfCards.toMutableList())
}

