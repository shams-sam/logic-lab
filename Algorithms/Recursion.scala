object Recursion {
  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }

  /**
   * Calculate pascal triangle value
   * given (column, row)
   * indexed from 0
   */
    def pascal(c: Int, r: Int): Int = {
      if (c == 0 || c == r) 1
      else pascal(c - 1, r - 1) + pascal(c, r - 1)
    }

  /**
   * Check if a given expression is paranthesis balanced
   * ()() is balanced
   * ())( is not balanced
   */
    def balance(chars: List[Char]): Boolean = {
      def loop(int: Int, chars: List[Char]): Int = {
        if (chars.isEmpty || int < 0) int
        else {
          chars.head match {
            case '(' => loop(int + 1, chars.tail)
            case ')' => loop(int - 1, chars.tail)
            case _  => loop(int, chars.tail)
          }
        }
      }
      if (loop(0, chars) != 0) false
      else true
    }

  /**
   * Calculate the number of ways 
   * one can tender changes 
   * given amount and coin denominations
   */
    def countChange(money: Int, coins: List[Int]): Int = {
      if (money == 0) 1
      else if (money < 0 || coins.length == 0) 0
      else countChange(money - coins.head, coins) +
        countChange(money, coins.tail)
    }
  }
