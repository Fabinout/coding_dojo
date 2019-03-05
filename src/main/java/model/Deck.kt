package model

class Deck(private val cards : MutableList<Card>) {

    fun size() : Int = cards.size

    fun shuffle(): Unit {
        cards.shuffle()
    }

    fun pick(): Card {
        return cards.removeAt(0);
    }

    fun peek(): Card {
        return cards.elementAt(0);
    }

}