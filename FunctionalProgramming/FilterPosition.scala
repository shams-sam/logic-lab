object FilterPosition {
    def f(arr: List[String]): List[String] = {
        arr.zipWithIndex.filter(_._2 % 2 != 0).map(_._1)
    }

    def main(args: Array[String]): Unit = {
        val arr = io.Source.stdin.getLines().takeWhile(_ != "").toList
        f(arr).map(i => println(i))
    }
}